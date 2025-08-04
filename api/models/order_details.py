from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    menu_item_id = Column(Integer, ForeignKey("menu_item.id"))
    amount = Column(Integer, index=True, nullable=False)
    menu_item_name = Column(String, ForeignKey("menu_item.name"))


    orders = relationship("Order", back_populates="order_details")
    menu_items_by_name = relationship("MenuItem", back_populates="order_details_by_name")
    menu_items_by_id = relationship("MenuItem", back_populates="order_details_by_id")
