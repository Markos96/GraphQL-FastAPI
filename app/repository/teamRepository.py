from app.model.Team import Team
from app.config.db import SessionLocal
from graphql import GraphQLError
from fastapi import status
import logging

session = SessionLocal()
logging = logging.getLogger(__name__)


def getAllTeams():
    try:
        teams = session.query(Team).all()

        if not teams:
            raise GraphQLError("Teams not found in database",
                               extensions={"code": status.HTTP_404_NOT_FOUND})
    except Exception as error:
        raise Exception(f"An error occurred while query {error}")

    return teams


def getTeamById(teamID):
    try:
        team = session.query(Team).get(teamID)

        if not team:
            raise GraphQLError("Team not found in database")

    except Exception as error:
        raise Exception(f"An error occurred while queries {error}")

    return team


def addTeam(teamInput):
    try:
        team = Team(name=teamInput.get("name"), stadium=teamInput.get("stadium"),
                    id_league=teamInput.get("id_league"), nickname=teamInput.get("nickname"))

    except Exception as error:
        logging.error(f"An error occurred while adding team {error}")

    session.add(team)
    session.commit()

    return team


def deleteTeam(teamID):
    try:
        team = session.query(Team).get(teamID)

        if not team:
            raise GraphQLError("Team not found in database")

    except Exception as error:
        logging.error(f"An error occurred while deleting team {error}")
        raise Exception("An occurred error from query")

    session.delete(team)
    session.commit()


def modifiedTeam(teamInput, teamID):
    try:
        team = getTeamById(teamID)

        if not team:
            raise GraphQLError("Team not found in database",
                               extensions={"code": status.HTTP_404_NOT_FOUND})

        for key, value in teamInput.items():
            if hasattr(team, key) and value is not None:
                setattr(team, key, value)

        session.commit()

    except Exception as error:
        logging.error(f"An error occurred while getting team {error}")
        raise Exception("An occurred internal error")

    return team


def getTeamByName(teamName):
    try:
        team = session.query(Team). \
            filter(Team.name.like(f'%{teamName}%')) \
            .all()

        if not team:
            raise GraphQLError("Team not found in database")

    except Exception as error:
        logging.error(f"An error occurred while getting team {error}")
        raise Exception("An occurred internal error")

    return team
