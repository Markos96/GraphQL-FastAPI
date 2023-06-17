from ariadne import QueryType, MutationType, make_executable_schema
from ariadne.asgi import GraphQL
from app.resolvers.playerResolver import playerQueries
from app.resolvers.playerResolver import playerMutations
from app.resolvers.teamResolver import teamMutations
from app.resolvers.teamResolver import teamQueries
from app.resolvers.leagueResolver import leagueMutations
from app.resolvers.leagueResolver import leagueQueries
from app.schema.types import type_defs
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

query = QueryType()
mutation = MutationType()

query.set_field("players", playerQueries.resolver_players)
query.set_field("teams", teamQueries.resolver_get_Teams)
query.set_field("leagues", leagueQueries.resolver_get_leagues)
query.set_field("team", teamQueries.resolver_team_by_id)
query.set_field("player", playerQueries.resolver_player_by_id)
query.set_field("league", leagueQueries.resolver_get_by_id_league)
query.set_field("teamByName", teamQueries.resolver_team_by_name)
query.set_field("playersByTeam", playerQueries.resolver_playersByTeam)

mutation.set_field("createTeam", teamMutations.resolver_create_team)
mutation.set_field("createPlayer", playerMutations.resolver_create_player)
mutation.set_field("createLeague", leagueMutations.resolve_create_league)
mutation.set_field("deleteTeam", teamMutations.resolver_delete_team)
mutation.set_field("deletePlayer", playerMutations.resolver_delete_player)
mutation.set_field("deleteLeague", leagueMutations.resolve_delete_league)
mutation.set_field("modifiedLeague", leagueMutations.resolve_modified_league)
mutation.set_field("modifiedPlayer", playerMutations.resolver_modified_player)
mutation.set_field("modifiedTeam", teamMutations.resolver_modified_team)

schema = make_executable_schema(type_defs, query, mutation)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/graphql", GraphQL(schema=schema))

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
