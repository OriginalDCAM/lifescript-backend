from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_users_read():
    response = client.get("/api/v1/users/?skip=0&limit=100")
    assert response.status_code == 200
