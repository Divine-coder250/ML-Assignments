from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# Property Model
class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    price = Column(Integer)

    # Relationship with Tenant
    tenants = relationship("Tenant", back_populates="property")

# Tenant Model
class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    property_id = Column(Integer, ForeignKey("properties.id"))

    # Relationship with Property
    property = relationship("Property", back_populates="tenants")
