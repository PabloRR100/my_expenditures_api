# root/app/db/crud/expenses.py

from fastapi import Path, HTTPException
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session

from app.db.models import expenses as models
from app.db.schemas import expenses as schemas


class ExpenseCRUD:

    def __init__(self):
        super().__init__()

    @staticmethod
    def list_expenses(
        db: Session,
    ):
        """ List all the categories
        """
        return db.query(models.Expense).all()

    @staticmethod
    def get_expense_by_id(
        db: Session,
        expense_id: int = Path(..., title="Expense ID"),
    ):
        """ Filter expense by ID
        """
        return db.query(models.Expense).filter(
            models.Expense.id == expense_id
        ).first()

    # @staticmethod
    # def get_expense_by_category(
    #     db: Session,
    #     name: str = Path(..., title="Groceries"),
    # ):
    #     """ Filter categories by name
    #     """
    #     return db.query(models.Expense).filter(
    #         models.Expense.name == name
    #     ).first()

    @staticmethod
    def create_expense(
        db: Session,
        expense: schemas.Expense
    ):
        """ Create new expense
        """
        new_expense = models.Expense(**expense.dict())
        db.add(new_expense)
        db.commit()
        db.refresh(new_expense)
        return new_expense

    @staticmethod
    def update_expense_by_id(
        db: Session,
        expense_name: str,
        new_expense: models.Expense
    ):
        """ Update existing season
        """
        data = jsonable_encoder(new_expense)
        print(data, new_expense)
        expense = db.query(models.Expense).filter(
            models.Expense.name == expense_name
        ).first()

        if not expense:
            raise HTTPException(404, "NOT FOUND")
        expense.id = new_expense.id
        expense.name = new_expense.name
        db.commit()
        db.refresh(expense)
        return expense

    @staticmethod
    def remove_expense_by_id(
        db: Session,
        expense_id: int,
    ):
        """ Delete existing expense by id
        """
        print("ID: ", expense_id)
        expense = db.query(models.Expense).filter(
            models.Expense.id == expense_id
        ).first()
        if not expense:
            # TODO: Exception
            print("[INFO]: Not found!")
            return None
        db.delete(expense)
        db.commit()
        return expense

    # @staticmethod
    # def remove_expense_by_category(
    #     db: Session,
    #     category_name: str,
    # ):
    #     """ Delete existing expense by category
    #     """
    #     # TODO: Implement filtering by another class attribute
