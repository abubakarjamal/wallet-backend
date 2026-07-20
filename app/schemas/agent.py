from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal


class AgentCreate(BaseModel):
    full_name: str
    phone: str
    shop_id: int


class AgentUpdate(BaseModel):
    full_name: str | None = None
    phone: str | None = None
    shop_id: int | None = None


class AgentResponse(BaseModel):
    id: int
    full_name: str
    phone: str
    shop_id: int
    float_balance: Decimal
    cash_balance: Decimal
    created_at: datetime

    model_config = {
        "from_attributes": True
    }