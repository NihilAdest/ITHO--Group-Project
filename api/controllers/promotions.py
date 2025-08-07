from sqlalchemy.orm import Session
from api.models.promotions import Promotion
from api.schemas.promotions import Promotion, PromotionCreate, PromotionUpdate

def create_promotion(db: Session, promotion: PromotionCreate):
    new_promotion = Promotion(**promotion.dict())
    db.add(new_promotion)
    db.commit()
    db.refresh(new_promotion)
    return new_promotion

def get_all_promotions(db: Session):
    return db.query(Promotion).all()

def get_promotion_by_id(db: Session, promotion_id: int):
    return db.query(Promotion).filter(Promotion.id == promotion_id).first()

def update_promotion(db: Session, promotion_id: int, promotion: PromotionUpdate):
    db_promo = get_promotion_by_id(db, promotion_id)
    if not db_promo:
        return None
    for field, value in promotion.dict(exclude_unset=True).items():
        setattr(db_promo, field, value)
    db.commit()
    db.refresh(db_promo)
    return db_promo

def delete_promotion(db: Session, promotion_id: int):
    db_promo = get_promotion_by_id(db, promotion_id)
    if db_promo:
        db.delete(db_promo)
        db.commit()
        return True
    return False
