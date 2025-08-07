from fastapi.testclient import TestClient
from api.main import app
import random

client = TestClient(app)

def test_create_order_detail():
    sample_detail = {
        "order_id": 1,
        "menu_item_id": 1,
        "quantity": 2,
        "amount":12.99
    }

    response = client.post("/order_details/", json=sample_detail)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())

    assert response.status_code == 200
    data = response.json()
    assert data["order_id"] == sample_detail["order_id"]
    assert data["menu_item_id"] == sample_detail["menu_item_id"]
    assert data["quantity"] == sample_detail["quantity"]
