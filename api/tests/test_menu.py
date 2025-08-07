from fastapi.testclient import TestClient
from ..main import app
import pytest
from ..models import menu_item as model
from ..controllers import menu_item as controller

client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    session = mocker.Mock()
    return session

def test_create_menu(db_session):
    # test menu data
    menu_data = {
        "name": "Alfredo Pasta",
        "description": "Pasta",
        "price": 100,
        "calories": 250,
        "food_category": "Veg",
    }

    # create a menu object from the input (or use a schema if the controller expects it)
    menu_obj = model.MenuItem(**menu_data)

    created_menu = controller.create(db_session, menu_obj)

    # Assertions
    assert created_menu.name == "Alfredo Pasta"
    assert created_menu.description == "Pasta"
    assert created_menu.price == 100
    assert created_menu.calories == 250
    assert created_menu.food_category == "Veg"