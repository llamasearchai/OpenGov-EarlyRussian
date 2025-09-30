import pytest
from fastapi.testclient import TestClient
from opengov_earlyrussian.api.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_decline() -> None:
    response = client.post(
        "/decline", json={"noun": "книга", "gender": "feminine", "animate": False}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["винительный"] == "книгу"


def test_conjugate() -> None:
    response = client.post("/conjugate", json={"verb": "читать", "tense": "present"})
    assert response.status_code == 200
    data = response.json()
    assert "forms" in data
    assert data["forms"]["я"].endswith("ю")


def test_transliterate() -> None:
    response = client.post("/transliterate", json={"text": "Mikhail"})
    assert response.status_code == 200
    data = response.json()
    assert "Михаил" in data["russian"]


def test_alphabet() -> None:
    response = client.get("/alphabet/iotated")
    assert response.status_code == 200
    data = response.json()
    assert "letters" in data
    assert "Я" in data["letters"]
