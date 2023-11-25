#!/usr/bin/python3
"""listing all states from database"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Setting up connection to the database
    user_name = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user_name}:{password}@localhost:3306/{db_name}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    states = (session.query(State, City).filter(City.state_id == State.id)
              .order_by(State.id))

    for state, city in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
