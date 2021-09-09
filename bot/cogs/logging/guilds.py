from datetime import datetime
from typing import Optional

from discord import Member
from discord.ext.commands import Cog

from bot.components.bot import Raptor


class GuildLogging(Cog):
    def __init__(self, bot: Raptor) -> None:
        self.bot = bot

    async def get_log_channels(self, event: str, guild_id: int, in_channel: Optional[int] = None) -> list:
        config = await self.bot.get_module_config(guild_id, "logging")

        if not config:
            return []

        channel_ids = []

        for key, value in config.get("channels", {}).items():
            key = int(key)

            if in_channel and in_channel in value.get("exclude_channels", []):
                continue

            if inc_channels := value.get("include_channels"):
                if in_channel not in inc_channels:
                    continue

            exc = value.get("exclude")
            if exc is not None:
                if event in exc:
                    continue
                channel_ids.append(key)
                continue

            inc = value.get("include")
            if inc is not None:
                if event in inc:
                    channel_ids.append(key)

        channels = [self.bot.get_channel(id) for id in channel_ids]

        if len(channels) > 5:
            channels = channels[:5]

        return [channel for channel in channels if channel]

    async def log(self, event: str, guild_id: int, message: str, in_channel: Optional[int] = None) -> None:
        channels = await self.get_log_channels(event, guild_id, in_channel)

        for channel in channels:
            time = datetime.utcnow()
            time = time.replace(microsecond=0)
            await channel.send(f"[`{time.isoformat()}`] {message}")

    @Cog.listener()
    async def on_member_join(self, member: Member) -> None:
        join_ts = round(member.created_at.timestamp())

        await self.log(
            "MEMBER_JOIN",
            member.guild.id,
            f":inbox_tray: {member.mention} (**{member}**, `{member.id}`) joined (created <t:{join_ts}:R>, <t:{join_ts}:F>)"
        )

    @Cog.listener()
    async def on_member_leave(self, member: Member) -> None:
        await self.log(
            "MEMBER_LEAVE",
            member.guild.id,
            f":outbox_tray: {member.mention} (**{member}**, `{member.id}`) left"
        )
