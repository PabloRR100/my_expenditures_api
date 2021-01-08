# root/app/db/models/categories.py

from sqlalchemy import (
    Column, ForeignKey,
    Integer, String
)
from sqlalchemy.orm import relationship

from app.database import Base
from app.db.models.expenses import Expense


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
