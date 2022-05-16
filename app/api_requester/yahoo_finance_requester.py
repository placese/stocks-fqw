import yfinance as yf
from datetime import date, timedelta

aapl = yf.Ticker('AAPL')
print(yf.download('AAPL', start=date.today() - timedelta(days=729), end=date.today(), interval='60m'))
