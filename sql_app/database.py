# root/sql_app/database.py

""" SQLAlchemy parts 
Notes:
    - We'll make each request gets its own database connection session in a dependency
    - Each instance of the SessionLocal class will be a database session
    - Inherit from "Base" class to create each of the database models or classes (the ORM models)

    - Engine is the entrypoint to the database and create the entry pools
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Databases
databases = dict(
    sqlite=dict(
        url="sqlite:///./sql_app.db",
        engine_args={"check_same_thread": False}
    ),
    postgres=dict(
        url="postgresql://{user}:{password}@postgresserver/{db}",
        engine_args={}
    )
)

# This is the line to modify to use a different database
DATABASE = "sqlite"
SQLALCHEMY_DATABASE_URL = databases[DATABASE]["url"]
ENGINE = create_engine(
    databases[DATABASE]["url"],
    connect_args=databases[DATABASE]["engine_args"]
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=ENGINE
)

Base = declarative_base()

