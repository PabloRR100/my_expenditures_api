# root/sql_app/schemas.py

""" Create Pydantic models
Notes:
    - Creating data steps:
        - Create a SQLAlchemy model instance with coming data
        - Add instance to the dabase connection
        - Commit changes to database
        - Refresh intance to contain new data from database (like generated id)
"""

from fastapi import Path
from sqlalchemy.orm import Session

from . import models, schemas


# Seasons
# -------

class SeasonCRUD:

    def list_seasons(
        db: Session, 
        skip: int = 0, limit: int = 50
    ):
        """ List all the seasons
        """
        return db.query(models.Season).offset(skip).limit(limit).all()

    def get_season_by_id(
        db: Session, 
        season_id: int = Path(..., title="ID de la temporda"),
    ):
        """ Filter season by ID
        """
        return db.query(models.Season).filter(
            models.Season.id == season_id
        ).first()

    def get_season_by_year(
        db: Session, 
        years: str = Path(..., title="Años"),
    ):
        """ Filter season by years. Use format 2019-2020 for instance
        """
        return db.query(models.Season).filter(
            models.Season.years == years
        ).first()

    def create_season(
        db: Session, 
        season: schemas.Season
    ):
        """ Create new season 
        """
        new_season = models.Season(**season.dict())
        db.add(new_season)
        db.commit()
        db.refresh(new_season)
        return new_season
        
    def update_season(
        db: Session, 
        season_id: str, 
        season: schemas.Season
    ):
        """ Update existing season 
        """
        return season



# Teams
# --------

class TeamCRUD:

    def list_teams(
        db: Session, 
        skip: int = 0, limit: int = 50
    ):
        """ List all teams
        """
        return db.query(models.Team).offset(skip).limit(limit).all()

    def get_team_by_id(
        db: Session, 
        team_id: int = Path(..., title="ID del equipo"),
    ):
        """ Filter team by ID
        """
        return db.query(models.Team).filter(
            models.Team.id == team_id
        ).first()

    def get_team_by_name(
        db: Session, 
        team_name: int = Path(..., title="Nombre del equipo"),
    ):
        """ Fitler team by name 
        """
        return db.query(models.Team).filter(
            models.Team.name == team_name
        ).first()

    def create_team(
        team: schemas.TeamCreate
    ):
        """ Create new team
        """
        new_team = models.Team(**team.dict())
        db.add(new_team)
        db.commit()
        db.refresh(new_team)
        return new_team

    def update_team(
        team_id: str, 
        team: schemas.TeamCreate
    ):
        """ Update existing team
        """
        return team

    def partial_update_team(
        team_id: str, 
        team: schemas.TeamCreate
    ):
        """ Partial update exisint team
        """
        return team



# Players
# --------

class PlayerCRUD:

    def list_players(
        db: Session, 
        skip: int = 0, limit: int = 50
    ):
        """ List all players 
        """
        return db.query(models.Player).offset(skip).limit(limit).all()

    def get_player_by_id(
        db: Session, 
        player_id: int = Path(..., title="ID del jugador"),
    ):
        """ Filter player by ID
        """
        return db.query(models.Player).filter(
            models.Player.id == player_id
        ).first()

    def get_player_by_name(
        db: Session, 
        team_name: int = Path(..., title="Nombre del jugador"),
    ):
        """ Filter player by name 
        """
        return db.query(models.Player).filter(
            models.Player.name == player_name
        ).first()

    def create_player(
        player: schemas.PlayerCreate
    ):
        """ Create new player
        """
        new_player = models.Player(**player.dict())
        db.add(new_player)
        db.commit()
        db.refresh(new_player)
        return new_player
