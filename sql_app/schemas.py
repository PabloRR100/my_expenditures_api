# root/sql_app/schemas.py

""" Create Pydantic models
Notes:
    - 
"""

from uuid import UUID
from typing import Optional, List, Set
from pydantic import BaseModel, Field, HttpUrl

from constants import Foot


# General


class Picture(BaseModel):
    id: UUID
    url: HttpUrl


class Shield(Picture):
    pass


class Stadium(BaseModel):
    id: UUID
    name: str
    capacity: int


# Season

class Season(BaseModel):
    id: UUID
    years: str = Field(..., example="2020-2021")


# Teams

class TeamBase(BaseModel):
    name: str = Field(..., example="Real Madrid")
    country: str = Field(..., example="España")


class TeamCreate(TeamBase):
    stadium: Stadium = Field(..., example="Bernabeu")
    shield: Optional[Shield] = None

class TeamOut(TeamBase):
    pass


class Team(TeamBase):
    id: UUID

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Real Madrid",
                "country": "España",
                "stadium": "Bernabeu",
                "shield": None
            }
        }

# Players


class PlayerBase(BaseModel):
    name: str = Field(..., example="Sergio Ramos")


class PlayerCreate(PlayerBase):
    age: int = Field(..., example=30)
    foot: Foot = Field(..., example=Foot.right)
    picture: Optional[Picture] = None
    

class PlayerOut(PlayerBase):
    pass


class Player(PlayerBase):
    id: UUID

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "Sergio Ramos",
                "age": 30,
                "foot": Foot.right,
                "picture": None,
            }
        }
