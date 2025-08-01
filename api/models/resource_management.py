from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class ResourceManagement(Base):
    __tablename__ = "resource_management"

    ingredient_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    unit = Column(String(255), nullable=False)
    current_stock = Column(DECIMAL(10,2))
    min_stock_level = Column(DECIMAL(10,2))
    cost_per_unit = Column(DECIMAL(10,2))
    restaurant_id = Column(Integer, ForeignKey("restaurants.restaurant_id"))

    restaurant = relationship("Restaurant", back_populates="resources")
