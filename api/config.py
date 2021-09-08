from functools import lru_cache
from os import environ
from pathlib import Path

from yaml import safe_load


@lru_cache()
def _get_local_config(location: str, guild_id: int) -> dict:
    fp = Path(location) / f"{guild_id}.yml"

    if not fp.exists():
        raise FileNotFoundError("The provided guild does not have a config file.")

    return safe_load(fp.read_text())


async def get_guild_config(guild_id: int) -> dict:
    provider = environ["CONFIG_PROVIDER"]

    type, location = provider.split(":")

    if type == "local":
        return _get_local_config(location, guild_id)

    raise ValueError("Invalid config provider set.")
