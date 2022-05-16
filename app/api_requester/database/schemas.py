from pydantic import BaseModel, Field
from datetime import datetime


class TickerDetailSchema(BaseModel):
    open: float = Field(...)
    high: float = Field(...)
    low: float = Field(...)
    close: float = Field(...)
    volume: float = Field(...)
    date_time: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "open": 0.0,
                "high": 0.0,
                "low": 0.0,
                "close": 0.0,
                "volume": 0.0,
                "date_time": "2020-01-01",
            }
        }


class TickerSchema(BaseModel):
    ticker: str = Field(...)
    time_stamps: list[TickerDetailSchema] = Field(...)
