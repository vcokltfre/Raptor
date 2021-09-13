from .api import APIConnector


class ConfigManager:
    def __init__(self, connector: APIConnector) -> None:
        self.connector = connector
        self.configs = {}

    async def get_config(self, guild_id: int) -> dict:
        if config := self.configs.get(guild_id):
            return config

        config = await self.connector.get(f"/guilds/{guild_id}/config")

        if not config:
            raise ValueError(f"Could not find config for guild: {guild_id}")

        self.configs[guild_id] = config_data = config["config"]

        return config_data

    async def update_config(self, guild_id: int) -> None:
        config = await self.connector.get(f"/guilds/{guild_id}/config")

        if not config:
            raise ValueError(f"Could not find config for guild: {guild_id}")

        self.configs[guild_id] = config["config"]
