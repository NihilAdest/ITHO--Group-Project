from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import review as controller
from ..schemas import review as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Review'],
    prefix="/reviews"
)

@router.post("/", response_model=schema.Review)
def create(request: schema.ReviewCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Review])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Review)
def read_one(review_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, review_id=review_id)


@router.put("/{item_id}", response_model=schema.Review)
def update(review_id: int, customer_id: int , request: schema.ReviewUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, review_id=review_id, customer_id=customer_id)


@router.delete("/{item_id}")
def delete(review_id: int, customer_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, review_id=review_id, customer_id=customer_id)
