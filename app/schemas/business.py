from pydantic import BaseModel
from datetime import datetime


class BusinessCreate(BaseModel):
    name: str
    paybill_number: str | None = None
    till_number: str | None = None
    phone: str


class BusinessUpdate(BaseModel):
    name: str | None = None
    paybill_number: str | None = None
    till_number: str | None = None
    phone: str | None = None


class BusinessResponse(BaseModel):
    id: int
    name: str
    paybill_number: str | None
    till_number: str | None
    phone: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }