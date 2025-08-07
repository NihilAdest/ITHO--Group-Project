from typing import Optional
from pydantic import BaseModel


class RestaurantBase(BaseModel):
    name: str
    address: str
    phone_number: str
    rating: Optional[float] = None
    opening_hours: str


class RestaurantCreate(RestaurantBase):
    pass


class RestaurantUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    rating: Optional[float] = None
    opening_hours: Optional[str] = None


class Restaurant(RestaurantBase):
    restaurant_id: int

    class Config:
        from_attributes = True
