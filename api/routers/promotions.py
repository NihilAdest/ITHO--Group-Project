from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.dependencies import get_db
from api.controllers import promotions as promotion_controller
from api.schemas.promotions import Promotion, PromotionCreate, PromotionUpdate
from typing import List

router = APIRouter(prefix="/promotions", tags=["Promotions"])

@router.post("/", response_model=Promotion, status_code=201)
def create_promotion(promotion: PromotionCreate, db: Session = Depends(get_db)):
    return promotion_controller.create_promotion(db, promotion)

@router.get("/", response_model=List[Promotion])
def read_promotions(db: Session = Depends(get_db)):
    return promotion_controller.get_all_promotions(db)

@router.get("/{promotion_id}", response_model=Promotion)
def read_promotion(promotion_id: int, db: Session = Depends(get_db)):
    promo = promotion_controller.get_promotion_by_id(db, promotion_id)
    if not promo:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promo

@router.put("/{promotion_id}", response_model=Promotion)
def update_promotion(promotion_id: int, promotion: PromotionUpdate, db: Session = Depends(get_db)):
    promo = promotion_controller.update_promotion(db, promotion_id, promotion)
    if not promo:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promo

@router.delete("/{promotion_id}", status_code=204)
def delete_promotion(promotion_id: int, db: Session = Depends(get_db)):
    success = promotion_controller.delete_promotion(db, promotion_id)
    if not success:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return
