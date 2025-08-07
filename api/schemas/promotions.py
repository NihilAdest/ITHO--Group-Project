from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PromotionBase(BaseModel):
    description: Optional[str]
    discount_type: Optional[str]
    discount_value: Optional[float]
    start_date: Optional[datetime]
    expiration_date: Optional[datetime]
    applicability: Optional[int]

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(PromotionBase):
    pass

class Promotion(PromotionBase):
    id: int

    class Config:
        from_attributes = True
