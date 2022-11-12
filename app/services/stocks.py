from app.services.yfinance import YFinanceService
from dataclasses import dataclass


@dataclass
class StocksService:
    def get_stock_details(self, stock_id: str):
        service = YFinanceService()
        return service.get_stock_details(stock_id)

    def get_stock_list(self):
        service = YFinanceService()
        return service.get_stock_list()
