from pydantic import BaseModel
from datetime import datetime

from app.models.enums import SMSStatus


class SMSNotificationCreate(BaseModel):
    transaction_id: int
    phone: str
    message: str


class SMSNotificationResponse(BaseModel):
    id: int
    transaction_id: int
    phone: str
    message: str
    sent_at: datetime
    status: SMSStatus

    model_config = {
        "from_attributes": True
    }