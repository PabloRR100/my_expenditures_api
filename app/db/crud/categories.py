# root/app/schemas.py

""" Create Pydantic models
Notes:
    - Creating data steps:
        - Create a SQLAlchemy model instance with coming data
        - Add instance to the database connection
        - Commit changes to database
        - Refresh instance to contain new data from database (like generated id)
"""

from fastapi import Path, HTTPException
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session

from app.db.models import categories as models
from app.db.schemas import categories as schemas


class CategoryCRUD:

    def __init__(self):
        super().__init__()

    @staticmethod
    def list_categories(
        db: Session, 
    ):
        """ List all the categories
        """
        return db.query(models.Category).all()

    @staticmethod
    def get_category_by_id(
        db: Session, 
        category_id: int = Path(..., title="ID de la categoría"),
    ):
        """ Filter category by ID
        """
        return db.query(models.Category).filter(
            models.Category.id == category_id
        ).first()

    @staticmethod
    def get_category_by_name(
        db: Session, 
        name: str = Path(..., title="Groceries"),
    ):
        """ Filter categories by name
        """
        return db.query(models.Category).filter(
            models.Category.name == name
        ).first()

    @staticmethod
    def create_category(
        db: Session, 
        category: schemas.Category
    ):
        """ Create new category
        """
        new_category = models.Category(**category.dict())
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return new_category

    @staticmethod
    def update_category_by_id(
        db: Session,
        category_name: str,
        new_category: models.Category
    ):
        """ Update existing season 
        """
        data = jsonable_encoder(new_category)
        print(data, new_category)
        category = db.query(models.Category).filter(
            models.Category.name == category_name
        ).first()

        if not category:
            raise HTTPException(404, "NOT FOUND")
        category.id = new_category.id
        category.name = new_category.name
        db.commit()
        db.refresh(category)
        return category

    @staticmethod
    def remove_category_by_id(
        db: Session,
        category_id: int,
    ):
        """ Delete existing category by id
        """
        print("ID: ", category_id)
        category = db.query(models.Category).filter(
            models.Category.id == category_id
        ).first()
        if not category:
            # TODO: Exception
            print("[INFO]: Not found!")
            return None
        db.delete(category)
        db.commit()
        return category

    @staticmethod
    def remove_category_by_name(
        db: Session,
        category_name: str,
    ):
        """ Delete existing category by name
        """
        print("Searching")
        category = db.query(models.Category).filter(
            models.Category.name == category_name
        ).first()
        if not category:
            # TODO: Exception
            print("[INFO]: Not FOund!")
            return None
        print("Cat", category)
        return CategoryCRUD.remove_category_by_id(db, category.id)

