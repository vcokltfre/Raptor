from datetime import datetime

from pydantic import BaseModel


class Log(BaseModel):
    data: dict


class LogResponse(BaseModel):
    id: int
    type: int
    data: dict
    created_at: datetime
