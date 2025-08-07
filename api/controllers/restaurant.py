from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..models.resturant import Restaurant
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = Restaurant(**request.dict())

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return new_item


def read_all(db: Session):
    return db.query(Restaurant).all()


def read_one(db: Session, restaurant_id: int):
    item = db.query(Restaurant).filter(Restaurant.restaurant_id == restaurant_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return item


def update(db: Session, restaurant_id: int, request):
    item = db.query(Restaurant).filter(Restaurant.restaurant_id == restaurant_id)
    if not item.first():
        raise HTTPException(status_code=404, detail="Restaurant not found")

    item.update(request.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return item.first()


def delete(db: Session, restaurant_id: int):
    item = db.query(Restaurant).filter(Restaurant.restaurant_id == restaurant_id)
    if not item.first():
        raise HTTPException(status_code=404, detail="Restaurant not found")

    item.delete(synchronize_session=False)
    db.commit()
    return {"detail": "Restaurant deleted"}
