from os import environ
from pathlib import Path

from aiohttp import ClientSession
from yaml import safe_load

from .cache import GuildConfigCache


CACHE = GuildConfigCache()

provider_string = environ["CONFIG_PROVIDER"]
p_type, p_location = provider_string.split(":", 1)

if p_type not in ["local", "http"]:
    raise ValueError("Invalid config provider set.")


@CACHE.cached
async def _get_local_config(guild_id: int) -> dict:
    fp = Path(p_location) / f"{guild_id}.yml"

    if not fp.exists():
        raise FileNotFoundError("The provided guild does not have a config file.")

    return safe_load(fp.read_text())


@CACHE.cached
async def _get_http_config(guild_id: int) -> dict:
    async with ClientSession() as session:
        resp = await session.get(p_location.format(guild_id=guild_id))
        text = await resp.text()

        return safe_load(text)


async def get_guild_config(guild_id: int) -> dict:
    provider = {
        "local": _get_local_config,
        "http": _get_http_config,
    }[p_type]

    return await provider(guild_id)
