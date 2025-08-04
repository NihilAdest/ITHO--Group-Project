from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PaymentBase(BaseModel):
    payment_type: str
    card_no: str
    transaction_status: str

class PaymentCreate(BaseModel):
    order_id: int
    amount: float

class PaymentUpdate(BaseModel):
    payment_type: Optional[str]
    card_no: Optional[str]
    transaction_status: Optional[str]

class Payment(PaymentBase):
    id: int
    payment_date: datetime
    class Config:
        from_attributes = True