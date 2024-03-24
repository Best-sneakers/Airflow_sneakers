from typing import Optional

from pydantic import BaseModel


class Sneaker(BaseModel):
    id: Optional[int] = None
    brand: str
    model: str
    size: float
    color: str
