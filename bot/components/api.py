from os import environ
from typing import Optional

from aiohttp import ClientSession


class APIConnector:
    def __init__(self) -> None:
        self.base_url = f"{environ['API_SCHEME']}://{environ['API_LOCATION']}:{environ['API_PORT']}"

        self._session: ClientSession = self.create_session()

    @staticmethod
    def create_session() -> ClientSession:
        return ClientSession(
            headers={
                "Authorization": environ["MAIN_API_KEY"],
            },
        )

    @property
    def session(self) -> ClientSession:
        if self._session and not self._session.closed:
            return self._session
        self._session = self.create_session()
        return self._session

    async def get(self, path: str, params: dict = {}) -> Optional[dict]:
        async with self._session.get(self.base_url + path, params=params) as session:
            if session.status == 200:
                return await session.json()
            return

    async def post(self, path: str, params: dict = {}) -> Optional[dict]:
        async with self._session.post(self.base_url + path, params=params) as session:
            if session.status == 200:
                return await session.json()
            return

    async def patch(self, path: str, params: dict = {}) -> Optional[dict]:
        async with self._session.patch(self.base_url + path, params=params) as session:
            if session.status == 200:
                return await session.json()
            return

    async def delete(self, path: str, params: dict = {}) -> Optional[dict]:
        async with self._session.delete(self.base_url + path, params=params) as session:
            if session.status == 200:
                return await session.json()
            return
