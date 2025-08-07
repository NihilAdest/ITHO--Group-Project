from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PromotionBase(BaseModel):
    description: str
    discount_type: str
    discount_value: float
    start_date: datetime
    expiration_date: datetime
    applicability: int

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(PromotionBase):
    pass

class Promotion(PromotionBase):
    id: int

    class Config:
        from_attributes = True
