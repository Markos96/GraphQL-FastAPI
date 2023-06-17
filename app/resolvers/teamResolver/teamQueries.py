from ariadne import QueryType
from app.repository import teamRepository

query = QueryType()


@query.field("teams")
def resolver_get_Teams(obj, info):
    teams = teamRepository.getAllTeams()
    return teams


@query.field("team")
def resolver_team_by_id(obj, info, teamID):
    team = teamRepository.getTeamById(teamID)
    return team


@query.field("teamByName")
def resolver_team_by_name(obj, info, teamName):
    team = teamRepository.getTeamByName(teamName)
    return team
