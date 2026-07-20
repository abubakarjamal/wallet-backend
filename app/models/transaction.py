from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey, Numeric
from datetime import datetime
from decimal import Decimal
from app.models.enums import TransactionType, TransactionStatus
from sqlalchemy import Enum

from app.database.base import Base


class Transaction(Base):

    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)

    transaction_code: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )

    sender_wallet_id: Mapped[int | None] = mapped_column(
        ForeignKey("wallets.id"),
        nullable=True
    )

    receiver_wallet_id:Mapped[int | None] = mapped_column(
        ForeignKey("wallets.id"),
        nullable=True
    )

    agent_id: Mapped[int | None] = mapped_column(
        ForeignKey("agents.id"),
        nullable=True
    )

    business_id: Mapped[int | None] = mapped_column(
        ForeignKey("businesses.id"),
        nullable=True
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    transaction_fee: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        default=Decimal("0.00")
    )

    transaction_type: Mapped[TransactionType] = mapped_column(
    Enum(TransactionType),
    nullable=False
    )

    status: Mapped[TransactionStatus] = mapped_column(
    Enum(TransactionStatus),
    default=TransactionStatus.PENDING,
    nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    # Relationships
    sender_wallet: Mapped["Wallet"] = relationship(
        "Wallet",
        foreign_keys=[sender_wallet_id],
        back_populates="sent_transactions"
    )

    receiver_wallet: Mapped["Wallet"] = relationship(
        "Wallet",
        foreign_keys=[receiver_wallet_id],
        back_populates="received_transactions"
    )

    agent: Mapped["Agent"] = relationship(
        "Agent",
        back_populates="transactions"
    )

    business: Mapped["Business"] = relationship(
        "Business",
        back_populates="transactions"
    )

    sms_notifications: Mapped[list["SMSNotification"]] = relationship(
    "SMSNotification",
    back_populates="transaction"
    )

    reversal: Mapped["Reversal | None"] = relationship(
    "Reversal",
    back_populates="transaction",
    uselist=False
    )