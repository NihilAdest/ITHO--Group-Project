from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(700))
    discount_type = Column(String(200))
    discount_value = Column(DECIMAL(10,2))
    start_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    expiration_date = Column(DATETIME)
    applicability = Column(Integer)
