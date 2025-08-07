from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import restaurant as schema
from ..controllers import restaurant as controller
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/restaurants",
    tags=["Restaurants"]
)


@router.post("/", response_model=schema.Restaurant)
def create(request: schema.RestaurantCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)


@router.get("/", response_model=list[schema.Restaurant])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{restaurant_id}", response_model=schema.Restaurant)
def read_one(restaurant_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, restaurant_id)


@router.put("/{restaurant_id}", response_model=schema.Restaurant)
def update(restaurant_id: int, request: schema.RestaurantUpdate, db: Session = Depends(get_db)):
    return controller.update(db, restaurant_id, request)


@router.delete("/{restaurant_id}")
def delete(restaurant_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, restaurant_id)
