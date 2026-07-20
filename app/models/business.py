from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime
from datetime import datetime

from app.database.base import Base


class Business(Base):

    __tablename__ = "businesses"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    paybill_number: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
        unique=True
    )

    till_number: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
        unique=True
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # Relationships
    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction",
        back_populates="business"
    )