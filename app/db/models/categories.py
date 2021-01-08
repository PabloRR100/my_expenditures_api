# root/app/models.py

""" Create SQLAlchemy models from the Base class
Notes:
    - SQLAlchemy uses the term "model" to refer to these classes and instances that interact with the database
        But, pydantic uses "model" to refer to the data validatoin, documentation classes and instances
"""

from sqlalchemy import (
    Column, ForeignKey,
    Integer, String,
)
from sqlalchemy.orm import relationship

from app.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    # relationship("Expense", back_populates="category")

