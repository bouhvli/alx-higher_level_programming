#!/usr/bin/python3
"""
this module prints all the city objects from db.
"""
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    meta = Base.metadata

    engine = create_engine(
       'mysql+mysqldb://{}:{}@localhost/{}'
       .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    output = session.query(City, State)\
        .join(State, City.state_id == State.id)\
        .order_by(City.id.asc())

    for city, state in output.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
