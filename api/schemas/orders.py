from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    description: str
    tracking_id: str
    status: str
    total_price: float


class OrderCreate(OrderBase):
    customer_name: str
    customer_id: int


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None
    customer_name: str
    customer_id: int

    class ConfigDict:
        from_attributes = True
