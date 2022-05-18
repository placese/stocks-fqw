from fastapi import FastAPI
from pydantic import BaseModel
import json
from pprint import pprint

from app.tickers.tickers import router as TickersRouter
from app.analysis.analizer import process_analysis

app = FastAPI()

app.include_router(TickersRouter, tags=["Ticker"], prefix="/ticker")


@app.get("/", tags=["Root"])
async def read_root():
    res = await process_analysis()
    return {"success": f"{res}"}
