from os import environ
from pathlib import Path
from typing import Type, TypeVar

from discord import AllowedMentions, Intents, Member, Message
from discord.ext.commands import Bot, Context
from loguru import logger

from common.redis import RedisClient

from .api import APIConnector
from .config import ConfigManager

T = TypeVar("T")


class Raptor(Bot):
    """A subclass of `discord.ext.commands.Bot` to add functionality."""

    def __init__(self) -> None:
        self.api = APIConnector()
        self.configs = ConfigManager(self.api)
        self.redis = RedisClient()

        super().__init__(
            command_prefix=self.get_prefix,
            help_command=None,
            intents=Intents.all(),
            chunk_guilds_at_startup=True,
            allowed_mentions=AllowedMentions(
                everyone=False,
                users=False,
                roles=False,
                replied_user=False,
            ),
            heartbeat_timeout=15,
            max_messages=None,
        )

        for directory in Path("./bot/cogs").iterdir():
            self.load_extension(str(directory).replace("/", "."))
            logger.info(f"Loaded extension: {directory}")

    async def get_prefix(self, message: Message) -> str:
        if not message.guild:
            return "!"

        guild = await self.configs.get_config(message.guild.id)

        return guild.get("prefix", "!")

    async def update_config(self, data: dict) -> None:
        guild_id = data["guild_id"]

        await self.configs.update_config(guild_id)

    async def start(self, *args, **kwargs) -> None:
        self.loop.create_task(self.redis.listen("bridge:config", self.update_config))

        await super().start(*args, **kwargs)

    async def get_module_config(self, guild_id: int, module: str, schema: Type[T]) -> T:
        config = await self.configs.get_config(guild_id)
        return schema(guild_id=guild_id, **config.get("plugins", {}).get(module, {}))

    async def get_level(self, guild_id: int, member: Member) -> int:
        config = await self.configs.get_config(guild_id)
        guild = self.get_guild(guild_id)

        if not guild:
            return 0

        if guild.owner_id == member.id:
            return 99999

        if not (levels := config.get("levels")):
            return 0

        member_levels = [levels.get(member.id, 0)]

        for role in member.roles:
            if role.id in levels:
                member_levels.append(levels[role.id])

        return max(member_levels)

    async def get_ctx_level(self, ctx: Context) -> int:
        if not ctx.guild:
            return 0

        return await self.get_level(ctx.guild.id, ctx.author)  # type: ignore

    def run(self) -> None:
        logger.info("Starting the bot...")

        super().run(environ["BOT_TOKEN"])
