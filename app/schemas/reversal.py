from pydantic import BaseModel
from datetime import datetime


class ReversalCreate(BaseModel):
    transaction_id: int
    reason: str


class ReversalResponse(BaseModel):
    id: int
    transaction_id: int
    reason: str
    reversed_at: datetime

    model_config = {
        "from_attributes": True
    }