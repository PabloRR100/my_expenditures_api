
from fastapi import FastAPI

from app.db.models import categories
from app.database import ENGINE
from app.routers.categories import router as router_categories

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

app.include_router(router_categories, prefix="/v1")


# Expenses
# --------
#
# if __name__ == '__main__':
#     uvicorn.run(app, host="0.0.0.0", port=8000)
#
