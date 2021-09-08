from asyncio import get_event_loop
from os import environ

from tortoise import Tortoise, run_async


TORTOISE_ORM = {
    "connections": {"default": environ["DB_URI"]},
    "apps": {
        "models": {
            "models": ["api.db.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


async def init():
    await Tortoise.init(TORTOISE_ORM)
    await Tortoise.generate_schemas()
