from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.api_requester.database.crud import (
    add_ticker,
    retrieve_tickers
)

from app.api_requester.database.schemas import (
    TickerSchema
)

router = APIRouter()


@router.post("/", response_description="Ticker added")
async def add_ticker_data(ticker: TickerSchema = Body(...)):
    ticker = jsonable_encoder(ticker)
    print(ticker)
    new_ticker = await add_ticker(ticker)
    return new_ticker


@router.get("/")
async def get_tickers():
    return await retrieve_tickers()
