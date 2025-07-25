from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    menu_item_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    price = Column(DECIMAL(10,2))
    calories = Column(Integer)
    food_category = Column(String)

    reviews = relationship("Review", back_populates="menu_item")
    order_details = relationship("OrderDetail", back_populates="menu_item")
