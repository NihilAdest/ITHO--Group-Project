from fastapi.testclient import TestClient
from api.main import app
import random

client = TestClient(app)

def test_create_menu_item():
    unique_id = random.randint(1000, 9999)

    sample_item = {
        "name": f"ITHO Burger {unique_id}",
        "description": "Our signature It's Too Hot Outside™ burger!",
        "price": 9.99,
        "calories": 700,
        "food_category": "Entree",
        "restaurant_id": 1
    }

    response = client.post("/menu_item/?admin_code=2hot0utside", json=sample_item)
    print("STATUS:", response.status_code)
    print("RESPONSE JSON:", response.json())

    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    data = response.json()
    assert data["name"] == sample_item["name"]
    assert data["description"] == sample_item["description"]
    assert data["price"] == sample_item["price"]
    assert "id" in data
