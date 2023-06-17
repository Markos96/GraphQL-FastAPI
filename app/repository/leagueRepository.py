from app.config.db import SessionLocal
from app.model.League import League
from graphql import GraphQLError

session = SessionLocal()


def create_league(leagueInput):
    league = League(name=leagueInput.get("name"))

    session.add(league)
    session.commit()

    return league


def modified_league(leagueInput, leagueID):
    try:
        league = session.query(League).get(leagueID)

        if not league:
            raise GraphQLError("The database does not contain players",
                               extensions={"code": 404})

        for key, value in leagueInput.items():
            if hasattr(league, key) and value is not None:
                setattr(league, key, value)

        session.commit()

    except Exception as error:
        raise Exception(f"Occurred during from database {error}")

    return league


def get_leagues():
    leagues = session.query(League).all()
    return leagues


def get_league_by_id(leagueID):
    league = session.query(League).get(leagueID)
    return league


def delete_league(leagueID):
    league = session.query(League).get(leagueID)

    session.delete(league)
    session.commit()

