from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import resources as model


def create(db: Session, request):
    new_item = model.Resource(**request.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def read_all(db: Session):
    return db.query(model.Resource).all()


def read_one(db: Session, item_id: int):
    item = db.query(model.Resource).filter(model.Resource.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Resource not found")
    return item


def update(db: Session, item_id: int, request):
    item = db.query(model.Resource).filter(model.Resource.id == item_id)
    if not item.first():
        raise HTTPException(status_code=404, detail="Resource not found")
    item.update(request.dict(exclude_unset=True))
    db.commit()
    return item.first()


def delete(db: Session, item_id: int):
    item = db.query(model.Resource).filter(model.Resource.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Resource not found")
    db.delete(item)
    db.commit()
    return {"message": "Resource deleted"}
