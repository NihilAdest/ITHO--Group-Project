from fastapi.testclient import TestClient
from api.main import app
import random

client = TestClient(app)

def test_create_order():
    sample_customer = {
        "id": 1,
        "name": "Gray Gonzalez",
        "password": "Breego9419088!",
        "email": "GrayG@example.com",
        "phone": "123-456-7890",
        "address": "1234 ITHO Blvd."
    }
    client.post("/customers/", json=sample_customer)

    sample_order = {
        "customer_id": 1,
        "customer_name": "Gray Gonzalez",
        "description": "Wants the ITHO Burger with a side of small fries.",
        "tracking_id": "track-1234",
        "status": "Pending",
        "total_price": 19.99
    }

    response = client.post("/orders/", json=sample_order)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())

    assert response.status_code == 200
    data = response.json()
    assert data["customer_id"] == sample_order["customer_id"]
    assert data["status"] == sample_order["status"]
    assert "id" in data
