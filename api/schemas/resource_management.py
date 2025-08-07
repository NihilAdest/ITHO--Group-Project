from typing import Optional
from pydantic import BaseModel

class ResourceManagementBase(BaseModel):
    name: str
    unit: str
    current_stock: float
    min_stock_level: float
    cost_per_unit: float
    restaurant_id: int

class ResourceManagementCreate(ResourceManagementBase):
    pass

class ResourceManagementUpdate(BaseModel):
    name: Optional[str] = None
    unit: Optional[str] = None
    current_stock: Optional[float] = None
    min_stock_level: Optional[float] = None
    cost_per_unit: Optional[float] = None
    restaurant_id: Optional[int] = None

class ResourceManagement(ResourceManagementBase):
    ingredient_id: int

    class Config:
        from_attributes = True
