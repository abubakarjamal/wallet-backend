from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session

from app.schemas.customer import CustomerCreate,CustomerResponse
from app.database.dependencies import get_db

from app.services.customer_service import CustomerService

router = APIRouter(
  prefix= '/customers',
  tags= ['Customers'],
)



@router.post('/',response_model=CustomerResponse)
async def create_customer(
  customer : CustomerCreate,
  db : Session = Depends(get_db)
):

    return CustomerService.create_customer(db, customer)


@router.get('/',response_model=list[CustomerResponse]) 
async def get_customers(
  db : Session = Depends(get_db)
):
    return CustomerService.get_customers(db)


  
@router.get('/{customer_id}',response_model=CustomerResponse) 
async def get_customer(
  customer_id : int,
  db : Session = Depends(get_db)
):
    return CustomerService.get_customer(db,customer_id)




@router.delete('/{customer_id}')
def delete_customer(
  customer_id : int,
  db : Session = Depends(get_db)
):

    return CustomerService.delete_customer(db,customer_id)