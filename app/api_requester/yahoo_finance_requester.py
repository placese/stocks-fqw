from wsgiref import validate
import yfinance as yf
from datetime import date, timedelta
import pandas as pd


async def get_ticker_from_api(ticker: str) -> dict:
    data = yf.download(ticker, start=date.today() - timedelta(days=721), end=date.today() - timedelta(days=1), interval='60m')
    return await validate_data(ticker, data)


async def validate_data(ticker: str, data: pd.DataFrame) -> dict:
    data.pop("Adj Close")
    data["time_stamp"] = pd.to_datetime(data.index)
    data.columns = data.columns.str.lower()
    data = data.to_dict("records") 
    validated_data = {
        "ticker": ticker,
        "data": data
    }
    return validated_data

