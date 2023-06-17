from ariadne import MutationType
from app.repository import leagueRepository

mutation = MutationType()


@mutation.field("createLeague")
def resolve_create_league(obj, info, leagueInput):
    league = leagueRepository.create_league(leagueInput)
    return league


@mutation.field("modifiedLeague")
def resolve_modified_league(obj, info, leagueInput, leagueID):
    league = leagueRepository.modified_league(leagueInput, leagueID)
    return league


@mutation.field("deleteLeague")
def resolve_delete_league(obj, info, leagueID):
    leagueRepository.delete_league(leagueID)


mutation_resolvers = {
    "createLeague": resolve_create_league,
    "deleteLeague": resolve_delete_league,
    "modifiedLeague": resolve_modified_league
}
