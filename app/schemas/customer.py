from pydantic import BaseModel
from datetime import datetime


class CustomerCreate(BaseModel):
    full_name: str
    phone: str
    national_id: str


class CustomerResponse(BaseModel):
    id: int
    full_name: str
    phone: str
    national_id: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }