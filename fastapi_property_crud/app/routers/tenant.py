from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import create_tenant, get_all_tenants, get_tenant_by_id, get_tenants_by_property, update_tenant, delete_tenant
from app.schemas import TenantCreate, TenantResponse
from typing import List

router = APIRouter()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new tenant
@router.post("/", response_model=TenantResponse)
def create_tenant_endpoint(tenant_data: TenantCreate, db: Session = Depends(get_db)):
    return create_tenant(db, tenant_data)

# Get all tenants
@router.get("/", response_model=List[TenantResponse])
def get_all_tenants_endpoint(db: Session = Depends(get_db)):
    return get_all_tenants(db)

# Get a tenant by ID
@router.get("/{tenant_id}/", response_model=TenantResponse)
def get_tenant_by_id_endpoint(tenant_id: int, db: Session = Depends(get_db)):
    return get_tenant_by_id(db, tenant_id)

# Get tenants by property ID
@router.get("/property/{property_id}/", response_model=List[TenantResponse])
def get_tenants_by_property_endpoint(property_id: int, db: Session = Depends(get_db)):
    return get_tenants_by_property(db, property_id)

# Update a tenant by ID
@router.put("/{tenant_id}/", response_model=TenantResponse)
def update_tenant_endpoint(tenant_id: int, tenant_data: TenantCreate, db: Session = Depends(get_db)):
    return update_tenant(db, tenant_id, tenant_data)

# Delete a tenant by ID
@router.delete("/{tenant_id}/", response_model=TenantResponse)
def delete_tenant_endpoint(tenant_id: int, db: Session = Depends(get_db)):
    return delete_tenant(db, tenant_id)
