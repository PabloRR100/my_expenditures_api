# root/app/schemas.py

""" Create Pydantic models
Notes:
    - 
"""

from uuid import UUID
from datetime import datetime

from typing import Optional, List, Set
from pydantic import BaseModel, Field

from constants import Category as ConstantCategory


# General

class Category(BaseModel):
    id: int
    name: ConstantCategory

    class Config:
        orm_mode = True


class Entity(BaseModel):
    id: int
    name: str = Field(..., example="Eroski")
    group_id: int
    category: Category

    class Config:
        orm_mode = True


class EntityGroup(BaseModel):
    id: int
    name: str = Field(..., example="Grocery Store")
    tag: str = Field(..., example="By app")
    entities: List[Entity] = []

    class Config:
        orm_mode = True


# Expenses
# --------


class ExpenseBase(BaseModel):
    pass


class Expense(BaseModel):
    id: int
    category: Category
    amount: float
    date: datetime
    computed: bool = Field(..., example=str(datetime.now()))

    class Config:
        orm_mode = True
        # schema_extra = {
        #     "example": {
        #         "To complete": True
        #     }
        # }
