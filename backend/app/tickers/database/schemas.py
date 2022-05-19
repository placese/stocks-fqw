from pydantic import BaseModel, Field
from datetime import datetime

from yfinance import Ticker


class PriceSchema(BaseModel):
    open: float = Field(...)
    close: float = Field(...)
    high: float = Field(...)
    low: float = Field(...)
    volume: float = Field(...)
    time_stamp: datetime = Field(...)


class TickerBaseSchema(BaseModel):
    ticker: str = Field(...)


class TickerSchema(TickerBaseSchema):
    ticker: str = Field(...)
    data: list[PriceSchema] = Field(...)