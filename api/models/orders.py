from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String, ForeignKey("customers.name"))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    tracking_id = Column(String(300), nullable=False)
    description = Column(String(300))
    status = Column(String(300))
    total_price = Column(DECIMAL(10,2))
    customer_id = Column(Integer, ForeignKey("customers.id"))

    order_details = relationship("OrderDetail", back_populates="orders")
    customer = relationship("Customer", back_populates="orders")
    payment = relationship("Payment", back_populates="orders")