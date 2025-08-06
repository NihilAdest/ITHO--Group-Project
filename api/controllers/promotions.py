from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import promotions as model
from sqlalchemy.exc import SQLAlchemyError

ADMIN_CODE = "2hot0utside"

def create(db: Session, request):
    new_item = model.Promotion(
        description = request.description,
        discount_type = request.discount_type,
        discount_value = request.discount_value,
        start_date = request.start_date,
        expiration_date = request.expiration_date,
        applicability = request.applicability
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session, admin_code: str):
    if admin_code != ADMIN_CODE:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not authorized')
    try:
        result = db.query(model.Promotion).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return result


def read_one(db: Session, promo_id: int, admin_code: str):
    if admin_code != ADMIN_CODE:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not authorized')

    try:
        item = db.query(model.Promotion).filter(model.Promotion.id == promo_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion ID not found")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return item


def update(db: Session, promo_id: int, request, admin_code: str):
    if admin_code != ADMIN_CODE:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")

    try:
        promo = db.query(model.Promotion).filter(model.Promotion.id == promo_id)
        if not promo.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion ID not found")

        update_data = request.dict(exclude_unset=True)
        promo.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return promo.first()


def delete(db: Session, promo_id: int, admin_code: str):
    if admin_code != ADMIN_CODE:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")

    try:
        promo = db.query(model.Promotion).filter(model.Promotion.id == promo_id).first()
        if not promo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion ID not found")
        db.delete(promo)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
