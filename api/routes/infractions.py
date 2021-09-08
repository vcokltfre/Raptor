from fastapi import APIRouter, HTTPException
from tortoise.exceptions import DoesNotExist

from common.constants import I_INFRACTION_TYPES

from ..db.models import Infraction
from ..models import Infraction as APIInfraction
from ..models import InfractionResponse
from ..snowflake import create_snowflake

router = APIRouter(prefix="/infractions")


@router.post("/")
async def create_infraction(infraction: APIInfraction) -> int:
    if infraction.type not in I_INFRACTION_TYPES:
        raise HTTPException(400, "Invalid infraction type.")

    id = create_snowflake()

    await Infraction.create(
        id=id,
        **infraction.dict(),
    )

    return id


@router.get("/{id}")
async def get_infraction(id: int) -> InfractionResponse:
    try:
        infraction = await Infraction.get(id=id)
    except DoesNotExist:
        raise HTTPException(404, "Invalid infraction.")

    return InfractionResponse(
        id=id,
        type=infraction.type,
        user_id=infraction.user_id,
        user_name=infraction.user_name,
        mod_id=infraction.mod_id,
        mod_name=infraction.mod_name,
        created_at=infraction.created_at,
        expires_at=infraction.expires_at,
        is_expired=infraction.is_expired,
        is_hidden=infraction.is_hidden,
        metadata=infraction.metadata,
    )
