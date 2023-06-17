from ariadne import QueryType
from app.repository import leagueRepository

query = QueryType()


@query.field("leagues")
def resolver_get_leagues(obj, info):
    leagues = leagueRepository.get_leagues()
    return leagues


@query.field("league")
def resolver_get_by_id_league(obj, info, leagueID):
    league = leagueRepository.get_league_by_id(leagueID)
    return league
