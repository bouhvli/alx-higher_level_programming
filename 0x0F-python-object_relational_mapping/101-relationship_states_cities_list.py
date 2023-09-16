#!/usr/bin/python3
"""
this module creates the State “California” with the
City “San Francisco” from the database.
"""
from relationship_city import Base, City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    meta = Base.metadata
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True, pool_recycle=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_city = session.query(State).order_by(State.id)
    for state in state_city:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()
