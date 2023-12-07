import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "Hello World"}


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert "Application is healthy" in response.json["message"]
