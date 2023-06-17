from ariadne import MutationType
from app.repository import playerRepository

mutation = MutationType()


@mutation.field("createPlayer")
def resolver_create_player(obj, info, playerInput):
    player = playerRepository.savePlayer(playerInput)
    return player


@mutation.field("modifiedPlayer")
def resolver_modified_player(obj, info, playerInput, playerID):
    player = playerRepository.modifiedPlayer(playerInput, playerID)
    return player


@mutation.field("deletePlayer")
def resolver_delete_player(obj, info, playerID):
    playerRepository.deletePlayer(playerID)
    return "Player deleted successfully"


mutation_resolvers = {
    "createPlayer": resolver_create_player,
    "deletePlayer": resolver_delete_player,
    "modifiedPlayer": resolver_modified_player
}
