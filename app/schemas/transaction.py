from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal

from app.models.enums import TransactionType, TransactionStatus


class TransactionCreate(BaseModel):
    sender_wallet_id: int | None = None
    receiver_wallet_id: int | None = None
    agent_id: int | None = None
    business_id: int | None = None

    amount: Decimal = Field(gt=0)
    transaction_fee: Decimal = Field(ge=0)

    transaction_type: TransactionType


class TransactionResponse(BaseModel):
    id: int
    transaction_code: str

    sender_wallet_id: int | None
    receiver_wallet_id: int | None
    agent_id: int | None
    business_id: int | None

    amount: Decimal
    transaction_fee: Decimal
    transaction_type: TransactionType
    status: TransactionStatus
    created_at: datetime

    model_config = {
        "from_attributes": True
    }