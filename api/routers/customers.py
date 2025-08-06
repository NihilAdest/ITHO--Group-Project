from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import customers as controller
from ..schemas import customers as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Customers'],
    prefix="/customers"
)


@router.post("/", response_model=schema.Customer)
def create(request: schema.CustomerCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Customer])
def read_all(admin_code: str, db: Session = Depends(get_db)):
    return controller.read_all(db=db, admin_code=admin_code)


@router.get("/{customer_id}", response_model=schema.Customer)
def read_one(customer_id: int, password: str, db: Session = Depends(get_db)):
    return controller.read_one(db=db, customer_id=customer_id, password=password)


@router.put("/{customer_id}", response_model=schema.Customer)
def update(name: str, password: str , request: schema.CustomerUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, name=name, password=password)


@router.delete("/{customer_id}")
def delete(customer_name: str, customer_password: str, db: Session = Depends(get_db)):
    return controller.delete(db=db, customer_name=customer_name, customer_password=customer_password)
