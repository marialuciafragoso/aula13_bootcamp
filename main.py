from sqlmodel import Field, Session, SQLModel, create_engine, text


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None

engine = create_engine("sqlite:///database.db", echo=True)

SQLModel.metadata.create_all(engine)

hero_1 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_2 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.commit()

with Session(engine) as session:
    # Sua consulta SQL
    statement = text("SELECT * FROM hero;")

    # Executando a consulta
    results = session.exec(statement)

    # Fetch dos resultados
    heroes = results.fetchall()

    # Imprimindo os resultados
    for hero in heroes:
        print(hero)