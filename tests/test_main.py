from fastapi.testclient import TestClient
from app.main import app, add

client = TestClient(app)

def test_add_function():
    assert add(2, 3) == 5

def test_add_endpoint():
    r = client.get("/add?a=3&b=4")
    assert r.status_code == 200
    assert r.json() == {"result": 7}

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert "message" in r.json()
