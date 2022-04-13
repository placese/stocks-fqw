from tracemalloc import start
import yfinance as yf
from enum import Enum
import pandas
from datetime import date
from dateutil.relativedelta import relativedelta

class Period(Enum):
    DAYS = 'd'
    MONTHS = 'mo'
    YEARS = 'y'
    YTD = 'ytd'
    MAX = 'max'

class Interval(Enum):
    DAYS = 'd'
    MONTHS = 'mo'
    MINS = 'm'
    HOURS = 'h'
    WEEKS = 'wk'



class Ticker():
    def __init__(self, ticker: str) -> None:
        self.ticker = yf.Ticker(ticker)

    def _parse_interval(self, interval: Interval, qty: int) -> None:
        """Set self interval from quantity and interval input to yfinance interval"""
        self.interval = f'{qty}{interval._value_}'

    def _parse_period(self, period: Period, qty: int | None = None) -> None:
        """Set self interval from quantity and interval input to yfinance interval"""
        self.period = f'{qty}{period._value_}' if qty else f'{period._value_}'

    def get_info(self) -> dict:
        """Returns info about ticker"""
        return self.ticker.info
    
    def get_data(self, interval: Interval = Interval.MINS,
                interval_qty: int = 1,
                period: Period = Period.MAX,
                period_qty: int | None = None) -> pandas.core.frame.DataFrame:
        """Returns ticker's data"""
        self._parse_interval(interval=interval, qty=interval_qty)
        self._parse_period(period=period, qty=period_qty)
        if self.interval == '1m':
            today = date.today()
            start_to_date = today - relativedelta(days=30)
            result = yf.download(
                    tickers=self.ticker.ticker,
                    interval=self.interval,
                    # period='1d',
                    start=start_to_date.strftime("%Y-%m-%d"),
                    end=(start_to_date + relativedelta(days=1)).strftime("%Y-%m-%d")
                )
            while True:
                start_to_date += relativedelta(days=1)
                result += yf.download(
                    tickers=self.ticker.ticker,
                    interval=self.interval,
                    # period='1d',
                    start=start_to_date.strftime("%Y-%m-%d"),
                    end=(start_to_date + relativedelta(days=1)).strftime("%Y-%m-%d")
                )
                
                print(result)
                if start_to_date == today:
                    break
            return result
            


if __name__ == '__main__':
    ticker = Ticker('v')
    result = ticker.get_data()
    print(result.Open)