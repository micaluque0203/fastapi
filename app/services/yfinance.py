from app.adapters import YFinanceAdapter
from dataclasses import dataclass


@dataclass
class YFinanceService:
    def get_stock_details(self, stock_id: str):
        adapter = YFinanceAdapter()
        response = adapter.get_ticker_by_id(stock_id)
        return response

    def get_stock_list(self):
        adapter = YFinanceAdapter()
        response = adapter.get_tickers()
        return response
