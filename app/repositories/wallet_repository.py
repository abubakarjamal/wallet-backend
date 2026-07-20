from sqlalchemy import select
from sqlalchemy.orm import Session

from app.schemas.wallet import WalletCreate
from app.models.wallet import Wallet




class WalletRepository:

    @staticmethod
    def create_wallet(
        db: Session,
        customer_id : int,
    ):
        db_wallet = Wallet(customer_id=customer_id)

        db.add(db_wallet)
        db.commit()
        db.refresh(db_wallet)

        return db_wallet


    @staticmethod
    def get_wallets(
        db : Session,
    ):

        wallets_smt = select(Wallet)

        result = db.execute(wallets_smt).scalars().all()

        return result


    @staticmethod
    def single_wallet(db : Session, wallet_id : int):

        wallet_smt = select(Wallet).where(
          Wallet.id == wallet_id
        )

        wallet = db.execute(
          wallet_smt).scalars().first()

        return wallet


    @staticmethod 
    def single_customer_wallet(
      db : Session, 
      customer_id : int
    ):

        customer_wallet_smt = select(Wallet).where(
          Wallet.customer_id == customer_id
        )

        result = db.execute(
          customer_wallet_smt).scalars().first()
      
        return result
        