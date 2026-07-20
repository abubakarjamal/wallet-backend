from sqlalchemy.orm import mapped_column,Mapped,relationship
from sqlalchemy import String,Integer,DateTime
from datetime import datetime 
from app.database.base import Base






class Customer(Base):

    __tablename__ = 'customers'


    id : Mapped[int] = mapped_column(primary_key=True)
  
    full_name: Mapped[str] = mapped_column(
    String(100),
    nullable=False
)
    phone : Mapped[str] = mapped_column(
      String(20),nullable=False,unique=True
    )
  
    national_id : Mapped[str] = mapped_column(
      String(20),nullable=False,
unique=True
    )

    created_at: Mapped[datetime] = mapped_column(
    DateTime,
    default=datetime.utcnow
)

    wallet : Mapped['Wallet'] = relationship(
      back_populates='customer',
      cascade="all, delete-orphan"
    )