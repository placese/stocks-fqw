import requests
from pprint import pprint
import enum

from  config import ALPHA_VANTAGE_API_KEY, ALPHA_VANTAGE_API_URL_BASE


class FunctionRequest(enum.Enum):
    """Functions for Alpha Vantage API"""

    time_series_intraday: str = 'TIME_SERIES_INTRADAY'
    time_series_daily: str = 'TIME_SERIES_DAILY'
    time_series_weekly: str = 'TIME_SERIES_WEEKLY'
    time_series_monthly: str = 'TIME_SERIES_MONTHLY'
    quote: str = 'GLOBAL_QUOTE'
    search: str = 'SYMBOL_SEARCH'

class IntervalRequest(enum.Enum):
    """Intervals for Alpha Vantage API"""

    min_1: str = '1min'
    min_5: str = '5min'
    min_15: str = '15min'
    min_30: str = '30min'
    min_60: str = '60min'


class AlphaVantageRequester:
    """
    Alpha Vantage Requester\n
    Gets ticker\n
    request_by period: returns datastructure from Alpha Vantage API\n
    info: returns info about ticker
    """

    def __init__(self, ticker: str) -> None:
        self.ticker = ticker

    def _generate_url(self, function: str, interval: str | None = None) -> str:
        if interval:
            return f'{ALPHA_VANTAGE_API_URL_BASE}function={function}&symbol={self.ticker}&interval={interval}&apikey={ALPHA_VANTAGE_API_KEY}'
        return f'{ALPHA_VANTAGE_API_URL_BASE}function={function}&symbol={self.ticker}&apikey={ALPHA_VANTAGE_API_KEY}'
        

    def _parse_response(self, response: dict) -> dict:
        """Returns only required data from response"""
        for key in ['Time Series (1min', 'Time Series (5min)', 'Time Series (15min)',
                    'Time Series (30min)', 'Time Series (60min)',
                    'Time Series (Daily)', 'Weekly Time Series', 'Monthly Time Series']:
            if key in response.keys():
                return response.get(key)

    def request_by_period(self, period: str) -> dict:
        """Returns parsed response dict from Alpha Vantage API"""
        return self._parse_response(requests.get(self._generate_url(function=period)).json())

    def info(self) -> dict:
        return requests.get(self._generate_url(function=FunctionRequest.quote.value)).json()

    def request_intraday_by_interval(self, interval: str) -> dict:
        return self._parse_response(requests.get(self._generate_url(function=FunctionRequest.time_series_intraday.value, interval=interval)).json())

if __name__ == '__main__':
    aapl = AlphaVantageRequester('aapl')
    # pprint(aapl.request_by_period(period=FunctionRequest.time_series_monthly.value))
    pprint(aapl.request_intraday_by_interval(interval=IntervalRequest.min_60.value))
