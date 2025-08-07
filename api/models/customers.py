from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
from .orders import Order

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)

    orders_by_id = relationship("Order", back_populates="customers_by_id", foreign_keys=[Order.customer_id])
    orders_by_name = relationship("Order", back_populates="customers_by_name", foreign_keys=[Order.customer_name])
    reviews = relationship("Review", back_populates="customer")
