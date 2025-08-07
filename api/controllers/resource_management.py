from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import resource_management as model
from ..schemas import resource_management as schema
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request: schema.ResourceManagementCreate):
    new_item = model.ResourceManagement(**request.dict())
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return new_item

def read_all(db: Session):
    try:
        return db.query(model.ResourceManagement).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

def read_one(db: Session, ingredient_id: int):
    item = db.query(model.ResourceManagement).filter(model.ResourceManagement.ingredient_id == ingredient_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return item

def update(db: Session, ingredient_id: int, request: schema.ResourceManagementUpdate):
    item = db.query(model.ResourceManagement).filter(model.ResourceManagement.ingredient_id == ingredient_id)
    if not item.first():
        raise HTTPException(status_code=404, detail="Ingredient not found")
    item.update(request.dict(exclude_unset=True))
    db.commit()
    return item.first()

def delete(db: Session, ingredient_id: int):
    item = db.query(model.ResourceManagement).filter(model.ResourceManagement.ingredient_id == ingredient_id)
    if not item.first():
        raise HTTPException(status_code=404, detail="Ingredient not found")
    item.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
