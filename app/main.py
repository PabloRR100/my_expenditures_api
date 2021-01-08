
from fastapi import FastAPI

from app.db.models import categories
from app.database import ENGINE

from app.routers.categories import router as router_categories
from app.routers.expenses import router as router_expenses
from app.routers.entities import router_entity, router_entity_group


# Create the database tables
categories.Base.metadata.create_all(bind=ENGINE)

# Initialize the FastAPI application
tags_metadata = [
    {
        "name": "Categories",
        "description": "All available categories",
    },
    {
        "name": "Expenses",
        "description": "Expenses",
    },
]

app = FastAPI(
    title="MyTransactions API",
    version="1.0.0",
    openapi_tags=tags_metadata
)

app.include_router(router_categories, prefix="/v1", tags=["Categories"])
app.include_router(router_entity, prefix="/v1", tags=["Entities"])
app.include_router(router_entity_group, prefix="/v1", tags=["Entity Groups"])
app.include_router(router_expenses, prefix="/v1", tags=["Expenses"])

