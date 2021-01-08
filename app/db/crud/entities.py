# root/app/db/crud/entities.py

from fastapi import Path, HTTPException
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session

from app.db.models import entities as models
from app.db.schemas import entities as schemas


class EntityCRUD:

    @staticmethod
    def list_entities(
        db: Session,
    ):
        """ List all the categories
        """
        return db.query(models.Entity).all()

    @staticmethod
    def get_entity_by_name(
        db: Session,
        entity_name: str = Path(..., title="Entity name"),
    ):
        """ Filter entity by ID
        """
        return db.query(models.Entity).filter(
            models.Entity.name == entity_name
        ).first()

    @staticmethod
    def create_entity(
        db: Session,
        entity: schemas.Entity
    ):
        """ Create new entity
        """
        new_entity = models.Entity(**entity.dict())
        db.add(new_entity)
        db.commit()
        db.refresh(new_entity)
        return new_entity

    @staticmethod
    def update_entity_by_id(
        db: Session,
        entity_name: str,
        new_entity: models.Entity
    ):
        """ Update existing season
        """
        data = jsonable_encoder(new_entity)
        print(data, new_entity)
        entity = db.query(models.Entity).filter(
            models.Entity.name == entity_name
        ).first()

        if not entity:
            raise HTTPException(404, "NOT FOUND")
        entity.id = new_entity.id
        entity.name = new_entity.name
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def remove_entity_by_name(
        db: Session,
        entity_name: str,
    ):
        """ Delete existing entity by id
        """
        print("ID: ", entity_name)
        entity = db.query(models.Entity).filter(
            models.Entity.name == entity_name
        ).first()
        if not entity:
            # TODO: Exception
            print("[INFO]: Entity not found!")
            return None
        db.delete(entity)
        db.commit()
        return entity


class EntityGroupCRUD:

    @staticmethod
    def list_entity_groups(
        db: Session,
    ):
        """ List all the categories
        """
        return db.query(models.EntityGroup).all()

    @staticmethod
    def get_entity_group_by_name(
        db: Session,
        entity_group_name: str = Path(..., title="Entity name"),
    ):
        """ Filter entity by ID
        """
        return db.query(models.EntityGroup).filter(
            models.EntityGroup.name == entity_group_name
        ).first()

    @staticmethod
    def create_entity(
        db: Session,
        entity_group: schemas.EntityGroup
    ):
        """ Create new entity
        """
        new_entity_group = models.EntityGroup(**entity_group.dict())
        db.add(new_entity_group)
        db.commit()
        db.refresh(new_entity_group)
        return new_entity_group

    @staticmethod
    def update_entity_group_by_id(
        db: Session,
        entity_group_name: str,
        new_entity_group: models.Entity
    ):
        """ Update existing season
        """
        data = jsonable_encoder(new_entity_group)
        print(data, new_entity_group)
        entity_group = db.query(models.EntityGroup).filter(
            models.Entity.name == entity_group_name
        ).first()

        if not entity_group:
            raise HTTPException(404, "NOT FOUND")
        entity_group.id = new_entity_group.id
        entity_group.name = new_entity_group.name
        db.commit()
        db.refresh(entity_group)
        return entity_group

    @staticmethod
    def remove_entity_by_name(
        db: Session,
        entity_group_name: str,
    ):
        """ Delete existing entity by id
        """
        print("ID: ", entity_group_name)
        entity_group = db.query(models.EntityGroup).filter(
            models.Entity.name == entity_group_name
        ).first()
        if not entity_group:
            # TODO: Exception
            print("[INFO]: Entity_Group not found!")
            return None
        db.delete(entity_group)
        db.commit()
        return entity_group
