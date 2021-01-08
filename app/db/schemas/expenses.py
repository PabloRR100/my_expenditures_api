# root/app/schemas/categories.py


from datetime import datetime
from pydantic import BaseModel, Field

from .categories import Category


class ExpenseBase(BaseModel):
    pass


class Expense(BaseModel):
    id: int
    category: Category
    amount: float
    date: datetime = Field(..., example=str(datetime.now()))
    computed: bool = Field(..., example=True)

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 0,
                "category": "Groceries",
                "amount": 10.50,
                "date": datetime.now(),
                "computed": True
            }
        }
