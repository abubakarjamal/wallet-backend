from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.schemas.customer import CustomerCreate




class CustomerRepository:


    @staticmethod 
    def create(db : Session, customer : CustomerCreate):

        db_customer = Customer(**customer.model_dump())

        db.add(db_customer)

        db.commit()

        db.refresh(db_customer)

        return db_customer

  
    @staticmethod
    def get_all(db : Session):

        customer__smt = select(Customer)

        results = db.execute(
          customer__smt).scalars().all()

        return results


    @staticmethod
    def get_single(db : Session, customer_id : int):


        single_customer = select(
          Customer).where(
          Customer.id == customer_id
        )

        results = db.execute(
          single_customer).scalars().first()

        return results

    

    @staticmethod
    def delete(db : Session, customer_id : int):

        customer_smt = select(Customer).where(
          Customer.id == customer_id)


        result = db.execute(
          customer_smt).scalars().first()
      
        if not result:
          return None
          
        db.delete(result)

        db.commit()

        return None