# root/app/models.py

""" Create SQLAlchemy models from the Base class
Notes:
    - SQLAlchemy uses the term "model" to refer to these classes and instances that interact with the database
        But, pydantic uses "model" to refer to the data validatoin, documentation classes and instances
"""

from datetime import datetime

from sqlalchemy import (
    Column, ForeignKey,
    Integer, String, Float,
    Boolean, DateTime
)
from sqlalchemy.orm import relationship

from app.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    # relationship("Expense", back_populates="category")


class EntityGroup(Base):
    __tablename__ = "entity_groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    tag = Column(String)

    entities = relationship("Entity", back_populates="group")


class Entity(Base):
    __tablename__ = "entities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    group_id = Column(Integer, ForeignKey("entity_groups.id"))

    group = relationship("EntityGroup", back_populates="entities")

    # entity_group = relationship("EntityGroup", back_populates="entities")
    # expense = relationship("Expense", back_populates="")


class Expense(Base):
    __tablename__ = "expenses"
    
    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer,  ForeignKey("categories.id"))
    date = Column(DateTime, default=datetime.now())
    amount = Column(Float)
    entity_id = Column(String, ForeignKey("entities.id"))
    computed = Column(Boolean, default=True)

    # category = relationship("Category", back_populates="")
    # entity = relationship("Entity", back_populates="entity")

