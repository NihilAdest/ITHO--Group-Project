from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import recipes as model


def create(db: Session, request):
    new_item = model.Recipe(**request.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def read_all(db: Session):
    return db.query(model.Recipe).all()


def read_one(db: Session, item_id: int):
    item = db.query(model.Recipe).filter(model.Recipe.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return item


def update(db: Session, item_id: int, request):
    item = db.query(model.Recipe).filter(model.Recipe.id == item_id)
    if not item.first():
        raise HTTPException(status_code=404, detail="Recipe not found")
    item.update(request.dict(exclude_unset=True))
    db.commit()
    return item.first()


def delete(db: Session, item_id: int):
    item = db.query(model.Recipe).filter(model.Recipe.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db.delete(item)
    db.commit()
    return {"message": "Recipe deleted"}
