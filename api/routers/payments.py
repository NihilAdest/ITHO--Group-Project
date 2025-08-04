from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import payments as controller
from ..schemas import payments as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Payments'],
    prefix="/payments"
)


@router.post("/", response_model=schema.Payment)
def create(request: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Payment])
def read_all(admin_code: str, db: Session = Depends(get_db)):
    return controller.read_all(db=db, admin_code=admin_code)


@router.get("/{item_id}", response_model=schema.Payment)
def read_one(item_id: int, password: int, db: Session = Depends(get_db)):
    return controller.read_one(db=db, password=password, item_id=item_id)


@router.put("/{item_id}", response_model=schema.Payment)
def update(name: str, password: str , request: schema.PaymentUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, name=name, password=password)


@router.delete("/{item_id}")
def delete(customer_name: str, customer_password: str, db: Session = Depends(get_db)):
    return controller.delete(db=db, customer_name=customer_name, customer_password=customer_password)
