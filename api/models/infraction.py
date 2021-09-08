from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Infraction(BaseModel):
    type: int
    user_id: int
    user_name: str
    mod_id: int
    mod_name: str
    expires_at: Optional[datetime] = None
    metadata: Optional[dict] = None


class InfractionResponse(BaseModel):
    id: int
    type: int
    user_id: int
    user_name: str
    mod_id: int
    mod_name: str
    created_at: datetime
    expires_at: Optional[datetime] = None
    is_expired: bool = False
    is_hidden: bool = False
    metadata: Optional[dict] = None
