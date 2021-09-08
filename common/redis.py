from json import dumps, loads
from os import environ

from aioredis import Redis, from_url
from loguru import logger


class RedisClient:
    def __init__(self) -> None:
        self.redis: Redis = from_url(environ["REDIS_URI"])

        logger.info("Redis session instantiated.")

    async def push_event(self, channel: str, data: dict) -> None:
        await self.redis.lpush(channel, dumps(data))

    async def _listen(self, channel: str, callback) -> None:
        while True:
            data = await self.redis.brpop([channel])
            await callback(loads(data[1]))

    async def listen(self, channel: str, callback) -> None:
        while True:
            try:
                await self._listen(channel, callback)
            except Exception as e:
                logger.error(f"Error while listening on redis: {e}")
