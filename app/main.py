from typing import Union

from fastapi import FastAPI
from app.services.stocks import StocksService

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/stocks")
def stocks():
    stock_service = StocksService()
    return stock_service.get_stock_list()

@app.get("/stocks/{stock_id}")
def read_stock(stock_id: str):
    stock_service = StocksService()
    return stock_service.get_stock_details(stock_id)