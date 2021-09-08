from pydantic import BaseModel


class Log(BaseModel):
    data: dict
