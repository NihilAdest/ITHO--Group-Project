from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import resource_management as controller
from ..schemas import resource_management as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["ResourceManagement"],
    prefix="/resource_management"
)

@router.post("/", response_model=schema.ResourceManagement)
def create(request: schema.ResourceManagementCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.ResourceManagement])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{ingredient_id}", response_model=schema.ResourceManagement)
def read_one(ingredient_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, ingredient_id)

@router.put("/{ingredient_id}", response_model=schema.ResourceManagement)
def update(ingredient_id: int, request: schema.ResourceManagementUpdate, db: Session = Depends(get_db)):
    return controller.update(db, ingredient_id, request)

@router.delete("/{ingredient_id}")
def delete(ingredient_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, ingredient_id)
