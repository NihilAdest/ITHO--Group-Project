from fastapi.testclient import TestClient
from ..main import app
import pytest
from ..controllers import promotions as controller
from ..models import promotions as model

client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    session = mocker.Mock()
    return session

def test_create_promo_code(db_session):
    promo_data = {
        "code": "FREEDRINK",
        "discount_type": "percentage",
        "discount_value": 10,
        "expiration_date": "2025-12-31T23:59:59",
        "usage_limit": 50,
        "min_order_value": 30
    }

    promo_obj = model.Promotion(**promo_data)
    created_promo = controller.create(db_session, promo_obj)

    assert created_promo.code == "FREEDRINK"
    assert created_promo.discount_value == 10
    assert created_promo.usage_limit == 50
