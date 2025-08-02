from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = 'menu_items'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(DECIMAL(10,2))
    calories = Column(Integer)
    food_category = Column(String(255), nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))

    reviews = relationship("Review", back_populates="menu_item")
    order_details = relationship("OrderDetail", back_populates="menu_items")
    Restaurant = relationship("Restaurant", back_populates="menu_items")
