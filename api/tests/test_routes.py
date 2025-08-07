import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_read_customers():
    response = client.get("/customers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_customer():
    customer_data = {
        "name": "Test User",
        "password": "securepass123",
        "email": "test@example.com",
        "phone": "1234567890",
        "address": "123 Test Lane"
    }

    response = client.post("/customers/", json=customer_data)
    assert response.status_code == 201
    assert response.json()["name"] == "Test User"

def test_relationship_debug():
    from api.dependencies import get_db
    from api.models.orders import Order
    from api.models.payments import Payment

    db = next(get_db())

    payment = db.query(Payment).first()
    order_from_payment = payment.orders_by_id if payment else None

    order = db.query(Order).first()
    payments_from_order = order.payments_by_id if order else None

    print("✅ Payment -> Order:", order_from_payment.id if order_from_payment else "None")
    print("✅ Order -> Payments:", [p.id for p in payments_from_order] if payments_from_order else "None")

    db.close()
