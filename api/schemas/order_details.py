from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .menu_item import MenuItems


class OrderDetailBase(BaseModel):
    amount: int


class OrderDetailCreate(BaseModel):
    order_id: int
    menu_item_id: int
    quantity: int
    amount: float

class OrderDetailOut(BaseModel):
    order_id: int
    menu_item_id: int
    quantity: int
    amount: float

    class Config:
        orm_mode = True

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    menu_item_id: Optional[int] = None
    menu_item_name: Optional[str] = None
    amount: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    menu_item: Optional[MenuItems] = None

    class ConfigDict:
        from_attributes = True


