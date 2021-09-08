from fastapi import APIRouter, HTTPException
from tortoise.exceptions import DoesNotExist

from ..config import get_guild_config
from ..models import GuildConfigResponse

router = APIRouter(prefix="/guilds")


@router.get("/{id}/config")
async def get_guild_config(id: int) -> GuildConfigResponse:
    try:
        data = await get_guild_config(id)
    except FileNotFoundError:
        raise HTTPException(404, "Invalid guild.")

    return GuildConfigResponse(config=data)
