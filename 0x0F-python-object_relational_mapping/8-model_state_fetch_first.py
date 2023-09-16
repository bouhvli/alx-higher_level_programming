#!/usr/bin/python3
"""
this module prints the first state object from the db
using SQLAlchemy.
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
    sel = select(State).order_by(State.id)
    r = connection.execute(sel)
    row = r.fetchone()
    if row is None:
        print('Nothing')
    else:
        print("{}:{}".format(row.id, row.name))
