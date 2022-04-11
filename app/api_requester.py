import yfinance as yf


class Ticker():
    def __init__(self, ticker: str) -> None:
        self.ticker = yf.Ticker(ticker)

    def get_info_by_ticker(self) -> dict:
        return self.ticker.info


if __name__ == '__main__':
    ticker = Ticker('appl')
    ticker.get_info_by_ticker()
