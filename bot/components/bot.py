from os import environ
from typing import Dict

from discord import Intents, AllowedMentions, Message
from discord.ext.commands import Bot
from loguru import logger

from .api import APIConnector


class Raptor(Bot):
    """A subclass of `discord.ext.commands.Bot` to add functionality."""

    def __init__(self) -> None:
        self.configs: Dict[int, dict] = {}
        self.api = APIConnector()

        super().__init__(
            command_prefix=self.get_prefix,
            help_command=None,
            intents=Intents.all(),
            chunk_guilds_at_startup=False,
            allowed_mentions=AllowedMentions(
                everyone=False,
                users=False,
                roles=False,
                replied_user=False,
            ),
            heartbeat_timeout=15,
            max_messages=None,
        )

    async def get_prefix(self, message: Message) -> str:
        if not message.guild:
            return "!"

        guild = self.configs.get(message.guild.id)

        if not guild:
            logger.info(f"Fetching config for guild {message.guild.id} from the API...")
            config = await self.api.get(f"/guilds/{message.guild.id}/config")

            if not config:
                return "!"

            guild = config["config"]
            self.configs[message.guild.id] = guild
            logger.info(f"Loaded guild config for {message.guild.id}.")

        return guild.get("prefix", "!")

    def run(self) -> None:
        logger.info("Starting the bot...")

        super().run(environ["BOT_TOKEN"])
