from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal


class WalletCreate(BaseModel):
    customer_id: int


class WalletUpdate(BaseModel):
    balance: Decimal


class WalletResponse(BaseModel):
    id: int
    customer_id: int
    balance: Decimal
    created_at: datetime

    model_config = {
        "from_attributes": True
    }