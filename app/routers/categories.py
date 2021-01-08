
from typing import List, Union

from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session

from app.db.schemas import categories as schemas
from app.db.crud.categories import CategoryCRUD as CRUD
from app.database import get_db


router = APIRouter()


# Categories
# ----------

# List Categories
@router.get(
    "/categories/",
    summary="List Categories",
    tags=["Categories"],
    response_model=List[schemas.Category]
)
def list_categories(
        db: Session = Depends(get_db),
):
    return CRUD.list_categories(
        db=db,
    )


# # Filter categories by id
# @router.get(
#     "/categories/{category_id}",
#     summary="Get Category by id",
#     tags=["Categories"],
#     response_model=schemas.Category
# )
# def get_category_by_id(
#         category_id: int = Path(..., title="Category_id"),
#         db: Session = Depends(get_db),
# ):
#     return CRUD.get_category_by_id(
#         db=db, category_id=category_id
#     )


# Filter categories by years
@router.get(
    "/categories/{category_name}",
    summary="Get Category by Name",
    tags=["Categories"],
    response_model=schemas.Category
)
def get_season_by_name(
    category_name: str = Path(..., name="Groceries"),
    db: Session = Depends(get_db),
):
    return CRUD.get_category_by_name(
        db=db, name=category_name
    )


# Create category
@router.post(
    "/categories/",
    status_code=201,
    summary="Create Category",
    tags=["Categories"],
    response_model=schemas.Category
)
def create_category(
        category: schemas.Category,
        db: Session = Depends(get_db),
):
    """
    Create a new category

    - **category**
    """
    return CRUD.create_category(db, category)


@router.put(
    "/categories/{category_name}",
    summary="Update Category",
    tags=["Categories"],
    response_model=schemas.Category
)
def update_category_by_name(
        category_name: str,
        category: schemas.Category,
        db: Session = Depends(get_db),
):
    # TODO: implement
    return CRUD.update_category_by_id(db, category_name, category)


@router.delete(
    "/categories/{category_name}",
    summary="Delete Category Name",
    tags=["Categories"],
    response_model=schemas.Category
)
def delete_category(
    # category_name: Union[int, str],
    category_name: str,
    db: Session = Depends(get_db),
):
    if isinstance(category_name, int):
        return CRUD.remove_category_by_id(db, category_name)
    elif isinstance(category_name, str):
        return CRUD.remove_category_by_name(db, category_name)
    else:
        raise HTTPException(
            status_code=404,
            detail="category_name must be either id (int) or name (str)"
        )
