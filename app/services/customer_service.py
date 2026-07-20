from sqlalchemy.orm import Session

from app.schemas.customer import CustomerCreate
from app.repositories.customer_repository import CustomerRepository
from app.repositories.wallet_repository import WalletRepository

from app.exceptions.handlers import NotFoundException



class CustomerService:



    @staticmethod
    def create_customer(db : Session, customer : CustomerCreate):

      customer = CustomerRepository.create(
        db=db,
        customer = customer,
      )
      
      WalletRepository.create_wallet(
        db=db,
        customer_id = customer.id,
      )
      
      
      return customer

  
  
    @staticmethod
    def get_customers(db : Session):


      result = CustomerRepository.get_all(
        db = db 
      )

      if not result:

        raise NotFoundException("Customer not found")

      return result


  
      
    @staticmethod
    def get_customer(db : Session,customer_id : int):


      result = CustomerRepository.get_single(
        db = db,
        customer_id = customer_id
      )
      
      return result


    @staticmethod 
    def delete_customer(db : Session, customer_id:int):

      
      customer = CustomerRepository.delete(
        db=db,
        customer_id = customer_id
      
      )

      return customer