from fastapi.testclient import TestClient
from api.main import app
import random

client = TestClient(app)

def test_create_customer():
    # this will generate a random number in case of duplicates
    unique_id = random.randint(1000, 9999)

    sample_customer = {
        "name": f"Gray{unique_id}",
        "password": "Breego9419088!",
        "email": f"GrayG{unique_id}@example.com",
        "phone": "123-456-7890",
        "address": "1234 ITHO Blvd."
    }

    response = client.post("/customers/", json=sample_customer)

    # in case of errors
    print("RESPONSE STATUS:", response.status_code)
    print("RESPONSE JSON:", response.json())

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == sample_customer["name"]
    assert data["email"] == sample_customer["email"]
    assert "id" in data
