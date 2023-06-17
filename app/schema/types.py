from ariadne import gql

type_defs = gql("""
    
    type Player{
        id: ID!
        name: String
        age: Int
        number: Int
        id_team: ID
    }

    type Team{
        id: ID!
        name: String
        stadium: String
        nickname: String
        players: [Player]
        id_league: ID
    }
    
    type League{
        id: ID!
        name: String
        teams: [Team]
    }
    
    input LeagueInput{
        name: String
    }
    
    input TeamInput{
        name: String
        stadium: String
        nickname: String
        id_league: ID
    }
    
    input PlayerInput{
        name: String
        age: Int
        number: Int
        id_team: ID
    }

    type Query{
        players: [Player]
        teams: [Team]
        leagues: [League]
        team(teamID: ID!): Team
        player(playerID: ID!): Player
        league(leagueID: ID!): League
        teamByName(teamName: String): [Team]
        playersByTeam(teamID: ID!): [Player]
    }
    
    type Mutation{
        createTeam(teamInput: TeamInput): Team
        createPlayer(playerInput: PlayerInput): Player
        createLeague(leagueInput: LeagueInput): League
        modifiedLeague(leagueID: ID! , leagueInput: LeagueInput): League
        modifiedPlayer(playerID: ID! , playerInput: PlayerInput): Player
        modifiedTeam(teamID: ID! , teamInput: TeamInput): Team
        deleteTeam(teamID: ID!): String
        deletePlayer(playerID: ID!): String
        deleteLeague(leagueID: ID!): String
    }

""")
