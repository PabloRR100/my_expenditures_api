# root/sql_app/models.py

""" Create SQLAlchemy models from the Base class
Notes:
    - SQLAlchemy uses the term "model" to refer to these classes and instances that interact with the database
        But, pydantic uses "model" to refer to the data validatoin, documentation classes and instances
"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Picture(Base):
    __tablename__ = "pictures"
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)


class Shield(Base):
    __tablename__ = "shields"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)


class Stadium(Base):
    __tablename__ = "stadiums"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    capacity = Column(Integer)


class Season(Base):
    __tablename__ = "seasons"

    id = Column(Integer, primary_key=True, index=True)
    years = Column(String, primary_key=True, index=True, unique=True)


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, primary_key=True, index=True, unique=True)
    country = Column(String)
    shield_id = Column(Integer, ForeignKey("shields.id"))
    stadium_id = Column(Integer, ForeignKey("stadiums.id"))
    

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, primary_key=True, index=True, unique=True)
    age = Column(Integer)
    foot = Column(String)
    picture_id = Column(Integer, ForeignKey("pictures.id"))

