from fastapi.testclient import TestClient
from ..main import app
import pytest
from ..models import customers as model
from ..controllers import customers as controller

client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_customer(db_session):
    # Sample input data for a new customer
    customer_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "123-456-7890"
    }

    # Create a model object from the input (or use a schema if the controller expects it)
    customer_obj = model.Customer(**customer_data)

    # Call the controller method directly
    created_customer = controller.create(db_session, customer_obj)

    # Assertions
    assert created_customer is not None
    assert created_customer.name == "John Doe"
    assert created_customer.email == "john@example.com"
    assert created_customer.phone == "123-456-7890"
