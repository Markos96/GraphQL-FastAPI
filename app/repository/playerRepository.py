from app.config.db import SessionLocal
from graphql import GraphQLError
from fastapi import status
from app.model.Player import Player
import logging

session = SessionLocal()

logger = logging.getLogger(__name__)


def savePlayer(playerInput):
    try:
        player = Player(name=playerInput.get('name'), age=playerInput.get('age'),
                        number=playerInput.get('number'), id_team=playerInput.get('id_team'))

        session.add(player)
        session.commit()

    except Exception as error:
        logger.error("An error occurred in the query: %s", error)
        raise Exception(f"An unexpected error occurred {error}")

    return player


def getAllPlayers():
    try:
        players = session.query(Player).all()

        if not players:
            raise GraphQLError("No players found in session",
                               extensions={"code": status.HTTP_404_NOT_FOUND})

    except Exception as error:
        raise Exception(f"An unexpected error occurred {error}")

    return players


def getPlayerById(playerID):
    try:
        player = session.query(Player).get(playerID)

        if not player:
            raise GraphQLError("Player not exist in database",
                               extensions={"code": status.HTTP_404_404})

    except Exception as error:
        logger.error("An error occurred in the query: %s", error)
        raise Exception("An error occurred while fetching the player")

    return player


def get_by_player_by_team(teamID):
    players = session.query(Player) \
        .filter(Player.id_team == teamID) \
        .all()

    return players


def modifiedPlayer(playerInput, playerID):
    try:
        player = getPlayerById(playerID)

        if not player:
            raise GraphQLError("Player not exist in database",
                               extensions={"code": status.HTTP_404_404})

        for key, value in playerInput.items():
            if hasattr(player, key) and value is not None:
                setattr(player, key, value)

        session.commit()

    except Exception as error:
        logger.error("An error occurred in the query: %s", error)
        raise Exception("An error occurred while fetching the player")

    return player


def deletePlayer(playerID):
    try:
        player = getPlayerById(playerID)

        if not player:
            raise GraphQLError("Player not found in database",
                               extensions={"code": status.HTTP_404_NOT_FOUND})

        session.delete(player)
        session.commit()

    except Exception as error:
        logger.error(f"An error occurred in the query {error}")
        raise Exception("An occurred internal error")



