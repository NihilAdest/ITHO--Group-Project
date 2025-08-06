from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class CustomerBase(BaseModel):
    name: str
    password: str
    email: str
    phone: str
    address: str

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str]
    password: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    address: Optional[str]

class Customer(CustomerBase):
    id: int

    class Config:
        from_attributes = True