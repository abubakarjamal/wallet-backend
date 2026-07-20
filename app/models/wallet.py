from sqlalchemy.orm import mapped_column,Mapped,relationship
from sqlalchemy import String,Integer,DateTime,ForeignKey,Numeric
from datetime import datetime 
from decimal import Decimal 

from app.database.base import Base



class Wallet(Base):

    __tablename__ = 'wallets'

  
    id : Mapped[int] = mapped_column(primary_key=True)
  
    customer_id : Mapped[int] = mapped_column(
      ForeignKey('customers.id'),
      nullable=False,
      unique=True
)
  
    balance : Mapped[Decimal] = mapped_column(
      Numeric(12,2),
      default=0
    )

    created_at : Mapped[datetime] = mapped_column(
      DateTime,
      default=datetime.utcnow
    )


    customer : Mapped['Customer'] = relationship(
      back_populates='wallet'
    )

    sent_transactions: Mapped[list["Transaction"]] = relationship(
    "Transaction",
    foreign_keys="Transaction.sender_wallet_id",
    back_populates="sender_wallet"
    )
    
    received_transactions: Mapped[list["Transaction"]] = relationship(
    "Transaction",
    foreign_keys="Transaction.receiver_wallet_id",
    back_populates="receiver_wallet"
)