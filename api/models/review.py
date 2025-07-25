from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    menu_item_id = Column(Integer, ForeignKey("menu_items.menu_item_id"))
    review_text = Column(String)
    rating = Column(Integer)
    review_date = Column(DateTime, nullable=False, server_default=str(datetime.now()))

    customer = relationship("Customer", back_populates="reviews")
    menu_item = relationship("MenuItem", back_populates="reviews")
