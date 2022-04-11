from urllib import response
from fastapi.testclient import TestClient

from app.server import app

client = TestClient(app)


class TestGet:
    def test_get(self) -> None:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "oh hi"}
    
    def test_get_ticker_info(self) -> None:
        response = client.get("/tickers/appl")
        assert response.status_code == 200
    
