from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Restaurant(Base):
    __tablename__ = "restaurants"

    restaurant_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    address = Column(String)
    phone_number = Column(String)
    rating = Column(DECIMAL(10,2))
    opening_hours = Column(String)

    menu_items = relationship("MenuItem", back_populates="restaurant")
    orders = relationship("Order", back_populates="restaurant")
    resources = relationship("ResourceManagement", back_populates="restaurant")
