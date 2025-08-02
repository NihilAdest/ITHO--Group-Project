from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    payment_type = Column(String(300))
    card_no = Column(String(300))
    amount = Column(DECIMAL(10,2), ForeignKey("orders.total_price"))
    transaction_status = Column(String(300))
    payment_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))

    orders_by_id = relationship("Order", back_populates="payments_by_id", foreign_keys=[order_id])
    orders_by_total_price = relationship("Order", back_populates="payments_by_total_price", foreign_keys=[amount])