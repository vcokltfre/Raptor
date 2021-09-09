from datetime import datetime
from os import getenv

from discord.ext.commands import Cog
from loguru import logger

from bot.components.bot import Raptor

CHANNEL_ID = getenv("BOT_LOGS_CHANNEL")


class InternalLogging(Cog):
    def __init__(self, bot: Raptor) -> None:
        self.bot = bot

    @Cog.listener()
    async def on_internal_log(self, type: str, message: str) -> None:
        if not CHANNEL_ID:
            return

        await self.bot.wait_until_ready()

        channel = self.bot.get_channel(int(CHANNEL_ID))

        if not channel:
            return

        await channel.send(f"`[{datetime.utcnow().isoformat()}]` `[{type}]` {message}")  # type: ignore
