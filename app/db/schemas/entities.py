# root/app/db/schemas/entities.py

from typing import Optional
from pydantic import BaseModel, Field


class Entity(BaseModel):
    id: int
    name: str = Field(..., example="Dia")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 0,
                "name": "Eroski"
            }
        }


class EntityGroup(BaseModel):
    id: int
    name: str = Field(..., example="Supermarket")
    tag: Optional[str] = Field(..., example="Regular")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 0,
                "name": "Supermarket",
                "tag": "Luxury"
            }
        }
