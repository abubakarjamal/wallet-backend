from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.wallet import WalletCreate,WalletResponse,WalletUpdate
from app.services.wallet_service import WalletService

router = APIRouter(
    prefix='/wallets',
    tags= ['/Wallets'],
)






@router.get('/',response_model=list[WalletResponse])
async def get_wallets(db : Session = Depends(get_db)):

    return WalletService.get_wallets(db)



@router.get('/{wallet_id}',response_model=WalletResponse)
def get_wallet(wallet_id : int , db : Session = Depends(get_db)):

    return WalletService.get_wallet(db, wallet_id)



@router.get('/customer/{customer_id}',response_model=WalletResponse)

def customer_wallet(customer_id : int, db : Session = Depends(get_db)):

    return WalletService.customer_wallet(db, customer_id)