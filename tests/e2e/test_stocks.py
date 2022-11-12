import pytest
from fastapi.testclient import TestClient
from app.main import app
import json


@pytest.fixture
def test_client():
    return TestClient(app)


@pytest.fixture
def stock_by_id_APPLE():
    with open("tests/fixtures/apple_stock.json", "r") as appl_json:
        return json.load(appl_json)


@pytest.fixture
def fake_stocks():
    with open("tests/fixtures/stocks.json", "r") as appl_json:
        return json.load(appl_json)


def test_stocks_list(test_client, mocker, fake_stocks):
    mocker.patch("app.adapters.YFinanceAdapter.get_tickers", return_value=fake_stocks)
    response = test_client.get("/stocks")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_stocks_by_id(test_client, stock_by_id_APPLE, mocker):

    mocker.patch(
        "app.adapters.YFinanceAdapter.get_ticker_by_id", return_value=stock_by_id_APPLE
    )

    response = test_client.get("/stocks/AAPL")
    assert response.status_code == 200
    assert response.json().get("symbol") == "AAPL"
