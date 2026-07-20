from fastapi import FastAPI

from app.database.base import Base
from app.database.session import engine

import app.models  # This imports all models

from app.api.customers import router as customer_router
from app.api.wallets import router as wallet_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mpesa wallet API")

app.include_router(customer_router)
app.include_router(wallet_router)

@app.get("/")
def root():
    return {"message": "Mpesa Wallet API is running"}