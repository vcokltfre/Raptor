from pydantic import BaseModel


class GuildConfigResponse(BaseModel):
    config: dict
