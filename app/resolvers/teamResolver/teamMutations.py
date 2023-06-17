from ariadne import MutationType
from app.config.db import SessionLocal
from app.repository import teamRepository

session = SessionLocal()
mutation = MutationType()


@mutation.field("createTeam")
def resolver_create_team(obj, info, teamInput):
    team = teamRepository.addTeam(teamInput)
    return team


@mutation.field("modifiedTeam")
def resolver_modified_team(obj, info, teamInput, teamID):
    team = teamRepository.modifiedTeam(teamInput, teamID)
    return team


@mutation.field("deleteTeam")
def resolver_delete_team(obj, info, teamID):
    teamRepository.deleteTeam(teamID)
    return "Team deleted successfully"


mutation_resolvers = {
    "createTeam": resolver_create_team,
    "deleteTeam": resolver_delete_team,
    "modifiedTeam": resolver_modified_team
}
