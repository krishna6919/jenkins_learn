import pytest
from app import app

@pytest.fixture()
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"

def test_add(client):
    resp = client.get("/add?a=2&b=3")
    assert resp.status_code == 200
    assert resp.get_json()["sum"] == 5
