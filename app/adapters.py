import yfinance as yf
from dataclasses import dataclass


@dataclass
class YFinanceAdapter:
    stock_id: str = "aapl"  # not implemented

    def get_tickers(self):
        """
        Returns:
            tuple: returns a named tuple of Ticker objects

            # access each ticker using (example)
            tickers.tickers.MSFT.info
            tickers.tickers.AAPL.history(period="1mo")
            tickers.tickers.GOOG.actions
        """
        response = yf.Tickers("msft aapl goog")

        return [ticker.info for ticker in response.tickers.values()]

    def get_ticker_by_id(self, ticker_id: str):
        response = yf.Ticker(ticker_id)
        return response.info
