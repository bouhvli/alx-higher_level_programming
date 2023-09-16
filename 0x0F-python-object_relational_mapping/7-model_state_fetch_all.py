#!/usr/bin/python3
"""
this module lists all the states object from the database.
"""
from sqlalchemy import create_engine, select
import sys
from model_state import Base, State


if __name__ == '__main__':
    meta = Base.metadata
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    with engine.connect() as connection:
        sel = select(State).order_by(State.id)
        r = connection.execute(sel)
        for row in r:
            print("{}: {}".format(row.id, row.name))
        connection.close()
