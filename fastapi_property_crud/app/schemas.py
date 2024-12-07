from pydantic import BaseModel
from typing import List, Optional

# Property Schemas
class PropertyBase(BaseModel):
    name: str
    address: str
    price: int

class PropertyCreate(PropertyBase):
    name: str
    address: str
    price: int

class PropertyResponse(PropertyBase):
    id: int
    tenants: List["TenantResponse"] = []

    class Config:
        orm_mode = True

# Tenant Schemas
class TenantBase(BaseModel):
    name: str
    email: str
    property_id: int

class TenantCreate(TenantBase):
    pass

class TenantResponse(TenantBase):
    id: int

    class Config:
        orm_mode = True
