from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import promotions as controller
from ..schemas import promotions as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Promotions'],
    prefix="/promo-codes"
)

@router.post("/", response_model=schema.Promotion)
def create(request: schema.PromotionCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Promotion])
def read_all(admin_code: str, db: Session = Depends(get_db)):
    return controller.read_all(db=db, code=admin_code)

@router.get("/{id}", response_model=schema.Promotion)
def read_one(id: int, db: Session = Depends(get_db)):
    return controller.read(id=id, db=db)

@router.put("/{id}", response_model=schema.Promotion)
def update(id: int, request: schema.PromotionUpdate, db: Session = Depends(get_db)):
    return controller.update(id=id, request=request, db=db)

@router.delete("/{id}", response_model=schema.Promotion)
def delete(id: int, db: Session = Depends(get_db)):
    return controller.delete(id=id, db=db)