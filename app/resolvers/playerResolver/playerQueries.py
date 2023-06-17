from ariadne import QueryType
from app.repository import playerRepository

query = QueryType()


@query.field("players")
def resolver_players(obj, info):
    players = playerRepository.getAllPlayers()
    return players


@query.field("player")
def resolver_player_by_id(obj, info, playerID):
    player = playerRepository.getPlayerById(playerID)
    return player


@query.field("playersByTeam")
def resolver_playersByTeam(obj, info, teamID):
    players = playerRepository.get_by_player_by_team(teamID)
    return players
