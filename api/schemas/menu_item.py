from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class MenuItemBase(BaseModel):
    name: str
    description: str
    price: float
    calories: int
    food_category: str

class MenuItemCreate(MenuItemBase):
    restaurant_id: int

class MenuItemUpdate(MenuItemBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[float] = None
    food_category: Optional[str] = None

class MenuItems(MenuItemBase):
    id: int
    restaurant_id: int

    class Config:
        from_attributes = True
