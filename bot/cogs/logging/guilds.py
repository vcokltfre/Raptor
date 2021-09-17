from datetime import datetime
from typing import Optional

from discord import Member
from discord.abc import GuildChannel
from discord.ext.commands import Cog
from loguru import logger

from bot.components.bot import Raptor
from common.schemas.logging import LoggingModel


class GuildLogging(Cog):
    def __init__(self, bot: Raptor) -> None:
        self.bot = bot

    async def get_config(self, guild_id: int) -> LoggingModel:
        return await self.bot.get_module_config(guild_id, "logging", LoggingModel)

    def get_log_context(
        self, event: str, config: LoggingModel, in_channel: Optional[int] = None
    ) -> list:
        channel_ids = []

        for key, value in config.channels.items():
            key = int(key)

            if value.exclude_channels:
                if in_channel and in_channel in value.exclude_channels:
                    continue

            if value.include_channels:
                if in_channel not in value.include_channels:
                    continue

            exc = value.exclude
            if exc is not None:
                if event in exc:
                    continue
                channel_ids.append(key)
                continue

            inc = value.include
            if inc is not None:
                if event in inc:
                    channel_ids.append(key)

        channels = [self.bot.get_channel(id) for id in channel_ids]

        if len(channels) > 5:
            channels = channels[:5]

        return [
            channel
            for channel in channels
            if isinstance(channel, GuildChannel) and channel.guild.id == config.guild_id
        ]

    def format_log(self, event: str, config: LoggingModel, **data) -> str:
        fmt = getattr(config.formats, event)

        for k, v in data.items():
            repl = f"#({k})"

            if isinstance(v, datetime):
                ts_format = config.formats.timestamp or "%Y-%m-%d %H:%M:%S"
                v = f"{v.strftime(ts_format)}"

            fmt = fmt.replace(repl, v)

        return fmt

    async def log(
        self, event: str, config: LoggingModel, in_channel: Optional[int] = None, **data
    ) -> None:
        logger.debug(
            f"[Module:Logging] Event `{event}` received in guild `{config.guild_id}`"
        )

        channels = self.get_log_context(event, config, in_channel)
        ts_format = config.formats.timestamp or "%Y-%m-%d %H:%M:%S"
        ts = f"[`{datetime.utcnow().strftime(ts_format)}`] "

        for channel in channels:
            await channel.send(f"{ts}{self.format_log(event, config, **data)}")

    @Cog.listener()
    async def on_member_join(self, member: Member) -> None:
        config = await self.get_config(member.guild.id)

        await self.log(
            "MEMBER_JOIN",
            config,
            member_mention=member.mention,
            member_name=member.name,
            member_disc=member.discriminator,
            member_id=str(member.id),
            member_created_at=member.created_at,
        )

    @Cog.listener()
    async def on_member_leave(self, member: Member) -> None:
        config = await self.get_config(member.guild.id)

        await self.log(
            "MEMBER_LEAVE",
            config,
            member_mention=member.mention,
            member_name=member.name,
            member_disc=member.discriminator,
            member_id=str(member.id),
            member_created_at=member.created_at,
        )
