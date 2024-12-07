from fastapi import FastAPI
from app.database import engine, Base
from app.routers import property, tenant

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Create the FastAPI app
app = FastAPI()

# Include routers
app.include_router(property.router, prefix="/properties", tags=["Properties"])
app.include_router(tenant.router, prefix="/tenants", tags=["Tenants"])
