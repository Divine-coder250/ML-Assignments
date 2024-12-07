from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import create_property, get_all_properties, get_property_by_id, update_property, delete_property
from app.schemas import PropertyCreate, PropertyResponse
from typing import List

router = APIRouter()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new property
@router.post("/", response_model=PropertyResponse)
def create_property_endpoint(property_data: PropertyCreate, db: Session = Depends(get_db)):
    return create_property(db, property_data)

# Get all properties
@router.get("/", response_model=List[PropertyResponse])
def get_all_properties_endpoint(db: Session = Depends(get_db)):
    return get_all_properties(db)

# Get a property by ID
@router.get("/{property_id}/", response_model=PropertyResponse)
def get_property_by_id_endpoint(property_id: int, db: Session = Depends(get_db)):
    return get_property_by_id(db, property_id)

# Update a property by ID
@router.put("/{property_id}/", response_model=PropertyResponse)
def update_property_endpoint(property_id: int, property_data: PropertyCreate, db: Session = Depends(get_db)):
    return update_property(db, property_id, property_data)

# Delete a property by ID
@router.delete("/{property_id}/", response_model=PropertyResponse)
def delete_property_endpoint(property_id: int, db: Session = Depends(get_db)):
    return delete_property(db, property_id)
