from uuid import UUID
from typing import Optional, List, Set

from sqlalchemy.orm import Session
from fastapi import FastAPI, Path, Query, Depends
from pydantic import BaseModel, Field, HttpUrl

from constants import Foot

from . import models, schemas
from .database import SessionLocal, ENGINE
from .crud import (
    SeasonCRUD,
    TeamCRUD,
    PlayerCRUD
)

# Create the database tables
models.Base.metadata.create_all(bind=ENGINE)

# Initialize the FastAPI application
app = FastAPI()


# Create a database session and close it after finishing.
def get_db():
    # Only the code prior to and including the yield statement 
    # is executed before sending a response
    db = SessionLocal()
    try:
        # The yielded value is what is injected into path 
        # operations and other dependencies
        yield db
    # The code following the yield statement is executed after 
    # the response has been delivered:
    finally:
        db.close()



# Seasons
# -------

# List Seasons
@app.get(
    "/seasons/", 
    summary="List Seasons",
    tags=["Seasons"],
    response_model=List[schemas.Season]
)
def list_seasons(
    skip: int = 0, limit: int = 50,
    db: Session = Depends(get_db), 
):
    return SeasonCRUD.list_seasons(
        db=db,
        skip=skip,
        limit=list
    )

# Filter season by id
@app.get(
    "/seasons/{season_id}", 
    summary="Get Season by id",
    tags=["Seasons"],
    response_model=schemas.Season
)
def get_season_by_id(
    season_id: int = Path(..., title="Season_id"),
    db: Session = Depends(get_db), 
):
    return SeasonCRUD.get_season_by_id(
        db=db, season_id=season_id
    )

# Filter season by years
@app.get(
    "/seasons/{season_years}", 
    summary="Get Season by years",
    tags=["Seasons"],
    response_model=schemas.Season
)
def get_season_by_year(
    years: str = Path(..., title="Years (yyyy-yyyy)"),
    db: Session = Depends(get_db), 
):
    return SeasonCRUD.get_season_by_year(
        db=db, years=years
    )


@app.post(
    "/season/", 
    status_code=201,
    summary="Create Season",
    tags=["Seasons"],
    response_model=schemas.Season
)
def create_season(
    season: schemas.Season,
    db: Session = Depends(get_db), 
):
    new_season = models.Season(years=season.years)
    db.add(new_season)
    db.commit()
    db.refresh(new_season)
    return new_season
    

@app.put(
    "/seasons/{season_id}",
    summary="Update Season",
    tags=["Seasons"],
    response_model=schemas.Season
)
def update_season(
    season_id: str, 
    season: schemas.Season,
    db: Session = Depends(get_db), 
):
    return season



# Teams
# --------


@app.post(
    "/teams/", 
    status_code=201,
    summary="Create Team",
    tags=["Teams"],
    response_model=schemas.TeamOut, 
)
def create_team(team: schemas.TeamCreate):
    return team

@app.put(
    "/teams/{team_id}",
    summary="Update Team",
    tags=["Teams"],
    response_model=schemas.TeamOut
)
def update_team(
    team_id: str, 
    team: schemas.TeamCreate
):
    return team

@app.patch(
    "/teams/{team_id}",
    summary="Partial update Team",
    tags=["Teams"],
    response_model=schemas.TeamOut
)
def partial_update_team(
    team_id: str, 
    team: schemas.TeamCreate
):
    return team

@app.get(
    "/teams/", 
    summary="List Teams",
    tags=["Teams"],
    response_model=List[schemas.TeamOut]
)
def read_teams():
     return {"foo": "teams"}



# Players
# --------


@app.post(
    "/players/", 
    status_code=201,
    summary="Create Player",
    tags=["Players"],
    response_model=schemas.PlayerOut,
)
def create_player(player: schemas.PlayerCreate):
    """ Create a player with the requiered information.  
    If you didn't know, you can create description in 
    markdown from the docstring xD
    """
    return player

@app.get(
    "/players/", 
    summary="List Players",
    tags=["Players"],
    response_model=List[schemas.PlayerOut]
)
def read_players():
     return {"foo": "players"}

