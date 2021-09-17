class GuildConfigCache:
    def __init__(self) -> None:
        self.guilds = {}

    def cached(self, func):
        async def wrapper(id: int) -> dict:
            if id in self.guilds:
                return self.guilds[id]
            result = await func(id)
            self.guilds[id] = result
            return result
        return wrapper

    def release(self, id: int) -> None:
        if id in self.guilds:
            del self.guilds[id]
