from fastapi.testclient import TestClient
from ..main import app
import pytest
from ..controllers import review as controller
from ..models import review as model

client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    session = mocker.Mock()
    return session

# review_id, customer_id, menu_item_id, review_text, rating, review_date

def test_review(db_session):
    review_data = {
        "review_id": 1,
        "customer_id": 1,
        "menu_item_id": 1,
        "review_test": "Test Review",
        "rating": 10,
        "review_date": "2020-01-10"
    }

    review_obj = model.Review(**review_data)

    created_review = controller.create(db_session, review_obj)

    assert created_review.review_id == 1
    assert created_review.customer_id == 1
    assert created_review.menu_item_id == 1
    assert created_review.review_test == "Test Review"
    assert created_review.rating == 10
    assert created_review.review_date == "2020-01-10"
