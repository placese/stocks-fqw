from fastapi import FastAPI
from pydantic import BaseModel

from .api_requester import Ticker

app = FastAPI()

class TickerModel(BaseModel):
    info: dict

@app.get("/")
async def index():
    return {"message": "oh hi"}

@app.get("/tickers/")
async def tickers():
    pass

@app.get("/tickers/{ticker}", response_model=dict)
async def ticker(ticker: str):
    return Ticker(ticker).get_info_by_ticker()
