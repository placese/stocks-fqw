from fastapi import FastAPI
from pydantic import BaseModel

from app.api_requester.database.tickers import router as TickersRouter

app = FastAPI()

app.include_router(TickersRouter, tags=["Ticker"], prefix="/ticker")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "STONCKS"}
