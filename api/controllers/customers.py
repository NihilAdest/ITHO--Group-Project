from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import customers as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.Customer(
        name = request.name,
        password = request.password,
        email = request.email,
        phone = request.phone,
        address = request.address,

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
    try:
        if not admin_code == '2hot0utside':
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not authorized')
        result = db.query(model.Customer).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Customer).filter(model.Customer.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, name, password, request):
    try:
        customer = db.query(model.Customer).filter(model.Customer.name == name)
        if not customer.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name not found!")
        if customer.first().password != password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password not match!")
        update_data = request.dict(exclude_unset=True)
        customer.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return customer.first()


def delete(db: Session, customer_name, customer_password):
    try:
        item = db.query(model.Customer).filter(model.Customer.name == customer_name)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name not found!")
        if item.first().password != customer_password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password not match!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
