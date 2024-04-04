from typing import Optional

from pydantic import BaseModel


class Location(BaseModel):
    address: Optional[str] = None
    lat: float = 51.4975
    lng: float = -0.1357
