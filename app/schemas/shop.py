from pydantic import BaseModel
from datetime import datetime


class ShopCreate(BaseModel):
    name: str
    phone: str
    location: str


class ShopUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None
    location: str | None = None


class ShopResponse(BaseModel):
    id: int
    name: str
    phone: str
    location: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }