from fastapi.testclient import TestClient
from api.main import app
import random

client = TestClient(app)

def test_create_order():
    sample_customer = {
        "id": 1,
        "name": "TestCustomer",
        "password": "test123",
        "email": "test@example.com",
        "phone": "1234567890",
        "address": "123 Test Lane"
    }
    client.post("/customers/", json=sample_customer)

    sample_order = {
        "customer_id": 1,
        "customer_name": "TestCustomer",
        "description": "Test order for unit testing",
        "tracking_id": "track-1234",
        "status": "Pending",
        "total_price": 49.99
    }

    response = client.post("/orders/", json=sample_order)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())

    assert response.status_code == 200
    data = response.json()
    assert data["customer_id"] == sample_order["customer_id"]
    assert data["status"] == sample_order["status"]
    assert "id" in data
