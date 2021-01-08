# root/app/models/expenses.py


from datetime import datetime

from sqlalchemy import (
    Column, ForeignKey,
    Integer, String, Float,
    Boolean, DateTime
)
from sqlalchemy.orm import relationship

from app.database import Base
from app.db.models.categories import Category




class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    date = Column(DateTime, default=datetime.now())
    amount = Column(Float)
    entity_id = Column(String, ForeignKey("entities.id"))
    computed = Column(Boolean, default=True)

    # category = relationship("Category", back_populates="")
    # entity = relationship("Entity", back_populates="entity")
