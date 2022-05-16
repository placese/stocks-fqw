from bson.objectid import ObjectId

from .database import ticker_collection, tickers_helper


async def retrieve_tickers() -> list[dict]:
    """Returns all tickers presented in the database"""
    tickers = []
    async for ticker in ticker_collection.find():
        tickers.append(tickers_helper(ticker))
    return tickers


async def add_ticker(ticker_data: dict) -> dict:
    """Add ticker to the database"""
    ticker = await ticker_collection.insert_one(ticker_data)
    new_ticker = await ticker_collection.find_one({"_id": ticker.inserted_id})
    return tickers_helper(new_ticker)
    
