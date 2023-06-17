## <u>Player CRUD project with:</u>
* FastAPI
* GraphQL
* Ariadne
* PostgreSQL
* SQLAlchemy

This is a sample project showing how to implement a CRUD (Create - Read - Update and Delete)
system for players using FastAPI, GraphQL with Aridadne and PostgreSQL as database.

---

## <u>Pre-requisites</u>

Make sure you have the following installed before running the project:

- Python 3.7 o superior
- PIP
- PostgreSQL

---

## <u>Environment configuration</u>

1. Clone this repository on your local machine

```bash
git clone https://github.com/user/name-repository.git
```

2. Go to the project root directory

```bash
cd name-repository
```

3. Create and activate environment (Optional)

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Configure the PostgreSQL database

```bash
* Create a PostgreSQL database
* Update details of conection in the file 'app/config.py'
```

6. Run the migrations of the PostgreSQL database

```bash
alembic upgrade head
```

7. Init server FastAPI

```bash
uvicorn main:app --reload
```

8. Open your browser and visit http://localhost:8000/graphql to access the GraphQL interface.

---

## <u>GraphQL queries</u>


### 1) View all players
```bash
query {
  players {
    id
    name
    number
    team
  }
}
```

---

#### 2) Search for a player by ID
```bash
query {
  player(playerId: 1) {
    id
    name
    number
    team
  }
}
```

---

#### 3) Create a new player
```bash
mutation {
  createPlayer(player_input: {
    name: "John Doe"
    number: 25
    team: "Team A"
  }) {
    id
    name
    number
    team
  }
}
```

---

#### 4) Update player 
```bash
mutation{
  updatePlayer(playerID: 1, player_input:{
  name: "John"
  number: 26
  team: "Team B"
}) {
  id
  name
  number
  team
  }
}
```

---

#### 5) Delete player 
```bash
mutation{
  deletePlayer(playerID: 2)
}
```

---

#### 6) Search for player by name
```bash
query{
  playerByName(playerName: "John")
}
```

---

#### 7) Search for player by team name
```bash
query{
  playerByTeam(teamName: "Team B")
}
```

---

## <u>Project structure</u>

* app
  * config
    * db.py: Contains the configuration for the database
  * core
    * config.py: Configuration of environment variables 
  * models
    * player.py: Definition of data models.
  * repository
    * player_repository.py: Implementation of the business logic
  * resolvers
    * mutations.py: Implementation resolvers of type mutations
    * queries.py: Implementation resolvers of type queries
  * schema
    * types.py: Implementation of the schema GraphQL
* migrations: Contains the database migrations using Alembic.
* alembic.ini: Alembic configuration for migrations.
* main.py: Entry point of the application

