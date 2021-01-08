# root/app/schemas/categories.py

""" Create Pydantic models
"""

from pydantic import BaseModel

from app.constants import Category as ConstantCategory


class Category(BaseModel):
    id: int
    name: ConstantCategory

    class Config:
        orm_mode = True
