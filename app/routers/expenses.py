
from typing import List, Union

from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session

from app.db.schemas import expenses as schemas
from app.db.crud.expenses import ExpenseCRUD
from app.database import get_db


router = APIRouter()


# expenses
# ----------

# List expenses
@router.get(
    "/expenses/",
    summary="List expenses",
    response_model=List[schemas.Expense]
)
def list_expenses(
        db: Session = Depends(get_db),
):
    return ExpenseCRUD.list_expenses(
        db=db,
    )


# Filter expenses by years
@router.get(
    "/expenses/{expense_id}",
    summary="Get Expense by ID",
    response_model=schemas.Expense
)
def get_expense_by_id(
    expense_id: int = Path(..., id=1),
    db: Session = Depends(get_db),
):
    return ExpenseCRUD.get_expense_by_id(
        db=db, expense_id=expense_id
    )


# Create Expense
@router.post(
    "/expenses/",
    status_code=201,
    summary="Create Expense",
    response_model=schemas.Expense
)
def create_expense(
        expense: schemas.Expense,
        db: Session = Depends(get_db),
):
    """
    Create a new Expense

    - **Expense**
    """
    return ExpenseCRUD.create_expense(db, expense)


@router.put(
    "/expenses/{expense_name}",
    summary="Update Expense",
    response_model=schemas.Expense
)
def update_expense_by_name(
        expense_name: str,
        expense: schemas.Expense,
        db: Session = Depends(get_db),
):
    # TODO: implement
    return ExpenseCRUD.update_expense_by_id(db, expense_name, expense)


@router.delete(
    "/expenses/{expense_id}",
    summary="Delete Expense Name",
    response_model=schemas.Expense
)
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
):
    return ExpenseCRUD.remove_expense_by_id(db, expense_id)