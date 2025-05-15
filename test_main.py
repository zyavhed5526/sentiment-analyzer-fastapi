from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_sentiment():
    response = client.post("/analyze", json={"text": "I love this!"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "positive"
