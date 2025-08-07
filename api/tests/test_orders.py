from fastapi.testclient import TestClient
from api.main import app
import random

client = TestClient(app)

def test_create_order():
    # Change this to match an existing customer_id in your test DB
    sample_order = {
        "customer_id": 1,
        "customer_name": "TestCustomer",
        "order_status": "Pending"
    }

    response = client.post("/orders/", json=sample_order)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())

    assert response.status_code == 200
    data = response.json()
    assert data["customer_id"] == sample_order["customer_id"]
    assert data["order_status"] == sample_order["order_status"]
    assert "id" in data
