from typing import Dict, List, Union

from pydantic import BaseModel

from .logging import LoggingModel


class Plugins(BaseModel):
    logging: LoggingModel


class ConfigSchema(BaseModel):
    prefix: Union[str, List[str]]
    levels: Dict[int, int]
    plugins: Plugins
