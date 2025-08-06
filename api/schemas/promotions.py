from pydantic import BaseModel
from datetime import datetime

class PromotionBase(BaseModel):
    code: str
    description: str
    discount_percent: float
    expiration_date: datetime

class PromotionCreate(PromotionBase):
    pass

class PromotionOut(PromotionBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
