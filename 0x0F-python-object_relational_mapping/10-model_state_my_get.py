#!/usr/bin/python3
"""
this module prints the state object with the name == the name passed
as an argument from the db.
"""
from sqlalchemy import create_engine, MetaData, select, Table
import sys
from model_state import Base, State


if __name__ == '__main__':
    meta = Base.metadata
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    connection = engine.connect()
    with engine.connect() as connection:
        sel = select(State).where(State.name == sys.argv[4]).order_by(State.id)
        r = connection.execute(sel)
        state = r.fetchone()
        if (state is None):
            print("Not found")
        else:
            print("{}".format(state.id))
