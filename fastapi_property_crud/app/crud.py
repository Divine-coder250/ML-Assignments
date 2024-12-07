from sqlalchemy.orm import Session
from app.models import Tenant, Property
from app.schemas import TenantCreate, PropertyCreate

# Tenant CRUD

# Create a new tenant
def create_tenant(db: Session, tenant_data: TenantCreate):
    db_tenant = Tenant(
        name=tenant_data.name,
        email=tenant_data.email,
        property_id=tenant_data.property_id
    )
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)
    return db_tenant

# Get all tenants
def get_all_tenants(db: Session):
    return db.query(Tenant).all()

# Get a tenant by ID
def get_tenant_by_id(db: Session, tenant_id: int):
    return db.query(Tenant).filter(Tenant.id == tenant_id).first()

# Get tenants by property ID
def get_tenants_by_property(db: Session, property_id: int):
    return db.query(Tenant).filter(Tenant.property_id == property_id).all()

# Update a tenant by ID
def update_tenant(db: Session, tenant_id: int, tenant_data: TenantCreate):
    db_tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if db_tenant:
        db_tenant.name = tenant_data.name
        db_tenant.email = tenant_data.email
        db_tenant.property_id = tenant_data.property_id
        db.commit()
        db.refresh(db_tenant)
    return db_tenant

# Delete a tenant by ID
def delete_tenant(db: Session, tenant_id: int):
    db_tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if db_tenant:
        db.delete(db_tenant)
        db.commit()
    return db_tenant

# Property CRUD

# Create a new property
def create_property(db: Session, property_data: PropertyCreate):
    db_property = Property(
        name=property_data.name,
        address=property_data.address,
        price=property_data.price
    )
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

# Get all properties
def get_all_properties(db: Session):
    return db.query(Property).all()

# Get a property by ID
def get_property_by_id(db: Session, property_id: int):
    return db.query(Property).filter(Property.id == property_id).first()

# Update a property by ID
def update_property(db: Session, property_id: int, property_data: PropertyCreate):
    db_property = db.query(Property).filter(Property.id == property_id).first()
    if db_property:
        db_property.name = property_data.name
        db_property.address = property_data.address
        db_property.price = property_data.price
        db.commit()
        db.refresh(db_property)
    return db_property

# Delete a property by ID
def delete_property(db: Session, property_id: int):
    db_property = db.query(Property).filter(Property.id == property_id).first()
    if db_property:
        db.delete(db_property)
        db.commit()
    return db_property
