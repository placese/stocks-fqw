from numpy import float64
from app.api_requester import Ticker, Interval, Period
import pandas

class TestAPIRequester:
    def __init__(self) -> None:
        self.ticker = Ticker('v')
    
    def test_get_data_with_max_period(self):
        expected_result = pandas.DataFrame.columns = ['Open', 'High',  ]
        assert self.ticker.get_data(interval=Interval.DAYS, interval_qty=1).Open == []