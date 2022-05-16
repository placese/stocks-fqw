import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.tickers

ticker_collection = database.get_collection('tickers_collection')


def tickers_helper(ticker) -> dict:
    return {
        "id": str(ticker["_id"]),
        "ticker": ticker["ticker"],
        "time_stamps": ticker["time_stamps"],
    }
