# root/app/db/routes/entities.py


from typing import List, Union

from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session

from app.db.schemas import entities as schemas
from app.db.crud.entities import EntityCRUD, EntityGroupCRUD
from app.database import get_db


router_entity = APIRouter()
router_entity_group = APIRouter()


# Entities
# --------

# List entities
@router_entity.get(
    "/entities/",
    summary="List entities",
    response_model=List[schemas.Entity]
)
def list_entities(
        db: Session = Depends(get_db),
):
    return EntityCRUD.list_entities(
        db=db,
    )


# Filter entities by years
@router_entity.get(
    "/entities/{entity_name}",
    summary="Get Entity by ID",
    response_model=schemas.Entity
)
def get_entity_by_id(
    entity_name: str = Path(..., id=1),
    db: Session = Depends(get_db),
):
    return EntityCRUD.get_entity_by_name(
        db=db, entity_name=entity_name
    )


# Create Entity
@router_entity.post(
    "/entities/",
    status_code=201,
    summary="Create Entity",
    response_model=schemas.Entity
)
def create_entity(
    entity: schemas.Entity,
    db: Session = Depends(get_db),
):
    return EntityCRUD.create_entity(db, entity)


@router_entity.put(
    "/entities/{entity_name}",
    summary="Update Entity",
    response_model=schemas.Entity
)
def update_entity_by_name(
):
    # TODO: implement
    return {"Status": "Not Implemented"}


@router_entity.delete(
    "/entities/{entity_name}",
    summary="Delete Entity Name",
    response_model=schemas.Entity
)
def delete_entity(
    entity_name: str,
    db: Session = Depends(get_db),
):
    return EntityCRUD.remove_entity_by_name(db, entity_name)


# Entity groups
# ------------

# List entity group
@router_entity_group.get(
    "/entity_groups/",
    summary="List entities",
    response_model=List[schemas.EntityGroup]
)
def list_entities(
        db: Session = Depends(get_db),
):
    return EntityGroupCRUD.list_entity_groups(
        db=db,
    )


# Filter entities by years
@router_entity_group.get(
    "/entity_groups/{entity_group_name}",
    summary="Get Entity Group by name",
    response_model=schemas.EntityGroup
)
def get_entity_by_id(
    entity_group_name: str = Path(..., id=1),
    db: Session = Depends(get_db),
):
    return EntityGroupCRUD.get_entity_group_by_name(
        db=db, entity_group_name=entity_group_name
    )


# Create Entity
@router_entity_group.post(
    "/entity_groups/",
    status_code=201,
    summary="Create Entity Group",
    response_model=schemas.EntityGroup
)
def create_entity(
    entity: schemas.Entity,
    db: Session = Depends(get_db),
):
    return EntityGroupCRUD.create_entity(db, entity)


@router_entity_group.put(
    "/entity_groups/{entity_group_name}",
    summary="Update Entity",
    response_model=schemas.EntityGroup
)
def update_entity_by_name(
):
    # TODO: implement
    return {"Status": "Not Implemented"}


@router_entity_group.delete(
    "/entity_groups/{entity_group_name}",
    summary="Delete Entity Name",
    response_model=schemas.EntityGroup
)
def delete_entity(
    entity_group_name: str,
    db: Session = Depends(get_db),
):
    return EntityGroupCRUD.remove_entity_by_name(db, entity_group_name)
