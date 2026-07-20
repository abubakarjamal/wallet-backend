from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey
from datetime import datetime
from app.models.enums import SMSStatus
from sqlalchemy import Enum


from app.database.base import Base


class SMSNotification(Base):

    __tablename__ = "sms_notifications"

    id: Mapped[int] = mapped_column(primary_key=True)

    transaction_id: Mapped[int] = mapped_column(
        ForeignKey("transactions.id"),
        nullable=False
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    message: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    sent_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    status: Mapped[SMSStatus] = mapped_column(
    Enum(SMSStatus),
    default=SMSStatus.PENDING,
    nullable=False
    )

    # Relationship
    transaction: Mapped["Transaction"] = relationship(
        "Transaction",
        back_populates="sms_notifications"
    )