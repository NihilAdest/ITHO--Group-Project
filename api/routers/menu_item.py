from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import menu_item as controller
from ..schemas import menu_item as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['MenuItem'],
    prefix="/menu_item"
)


@router.post("/", response_model=schema.MenuItems)
def create(admin_code: str, request: schema.MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request, admin_code=admin_code)


@router.get("/", response_model=list[schema.MenuItems])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db=db)


@router.get("/{item_id}", response_model=schema.MenuItems)
def read_one(name: str, db: Session = Depends(get_db)):
    return controller.read_one(db=db, name=name)


@router.put("/{item_id}", response_model=schema.MenuItems)
def update(name: str, admin_code: str , request: schema.MenuItemUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, name=name, admin_code=admin_code)


@router.delete("/{item_id}")
def delete(name: str, admin_code: str, db: Session = Depends(get_db)):
    return controller.delete(db=db, name=name, admin_code=admin_code)
