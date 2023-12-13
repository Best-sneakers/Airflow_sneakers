__all__ = "BaseOrjson"

from uuid import UUID

import orjson
from pydantic import BaseModel


# pylint: disable=no-member
def orjson_dumps(cls, *, default):
    return orjson.dumps(cls, default=default).decode()


# pylint: disable=no-member
class BaseOrjson(BaseModel):
    id: UUID

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
