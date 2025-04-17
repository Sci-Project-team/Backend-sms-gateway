import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_send_sms_without_api_key():
    response = client.post(
        "/sms",
        json={"phone_number": "+33612345678", "message": "Test message"}
    )
    assert response.status_code == 403

def test_send_sms_with_valid_api_key():
    response = client.post(
        "/sms",
        headers={"X-API-Key": "test_api_key"},
        json={"phone_number": "+33612345678", "message": "Test message"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["phone_number"] == "+33612345678"
    assert data["message"] == "Test message"
    assert "id" in data
    assert "status" in data

def test_get_inbox_with_valid_api_key():
    response = client.get(
        "/sms/inbox",
        headers={"X-API-Key": "test_api_key"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_logs_with_valid_api_key():
    response = client.get(
        "/logs",
        headers={"X-API-Key": "test_api_key"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)