from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.api_requester.yahoo_finance_requester import get_ticker_from_api

from app.tickers.database.crud import (
    add_ticker,
    retrieve_tickers
)

from app.tickers.database.schemas import (
    TickerBaseSchema
)

router = APIRouter()


@router.post("/", response_description="Ticker added")
async def add_ticker_data(ticker: TickerBaseSchema = Body(...)):
    ticker = jsonable_encoder(ticker)['ticker']
    ticker = await get_ticker_from_api(ticker)
    return await add_ticker(ticker)


@router.get("/")
async def get_tickers():
    return await retrieve_tickers()
