from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ReviewBase(BaseModel):
    review_text: str
    rating: int

class ReviewCreate(BaseModel):
    customer_id: int
    menu_item_id: int

class ReviewUpdate(BaseModel):
    review_text: Optional[str]
    rating: Optional[int]

class Review(ReviewBase):
    review_id: int
    customer_id: int
    menu_item_id: int
    review_date: datetime

    class ConfigDict:
        from_attributes = True
