from fastapi import APIRouter, HTTPException
from tortoise.exceptions import DoesNotExist

from common.constants import I_LOG_TYPES

from ..db.models import Log
from ..models import Log as APILog
from ..models import LogResponse
from ..snowflake import create_snowflake

router = APIRouter(prefix="/logs")


@router.post("/")
async def create_log(type: int, log: APILog) -> int:
    if type not in I_LOG_TYPES:
        raise HTTPException(400, "Invalid log type.")

    id = create_snowflake()

    await Log.create(
        id=id,
        type=type,
        data=log.data,
    )

    return id


@router.get("/{id}")
async def get_log(id: int) -> LogResponse:
    try:
        log = await Log.get(id=id)
    except DoesNotExist:
        raise HTTPException(404, "Invalid log.")

    return LogResponse(
        id=id,
        type=log.type,
        data=log.data,
        created_at=log.created_at,
    )
