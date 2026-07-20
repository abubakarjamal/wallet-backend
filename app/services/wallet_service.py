from sqlalchemy.orm import Session

from app.schemas.wallet import WalletCreate
from app.repositories.wallet_repository import WalletRepository

from app.exceptions.handlers import NotFoundException


class WalletService:

    @staticmethod
    def create_wallet(
        db: Session,
        customer_id: int,
    ):

        wallet = WalletCreate(customer_id=customer_id)

        return WalletRepository.create_wallet(
            db=db,
            wallet=wallet,
        )

    @staticmethod 
    def get_wallets(db : Session):

        return WalletRepository.get_wallets(db = db)


    @staticmethod
    def get_wallet(db : Session, wallet_id : int):

        wallet = WalletRepository.single_wallet(
          db = db,
          wallet_id = wallet_id
        )

        if not wallet:

          raise NotFoundException('wallet is unavailable')

        return wallet


    @staticmethod
    def customer_wallet(db : Session, customer_id : int):

        wallet = WalletRepository.single_customer_wallet(
          db = db,
          customer_id = customer_id
        )

        if not wallet:

          raise NotFoundException('customer wallet is unavailable')

        return wallet

        