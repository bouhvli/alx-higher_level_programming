#!/usr/bin/python3
"""
this module has a script that add a new object to the db.
"""
from sqlalchemy import create_engine, MetaData, select, Table, insert
import sys
from model_state import Base, State


if __name__ == '__main__':
    meta = Base.metadata

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    connection = engine.connect()

    with engine.connect() as connection:
        new_value = insert(State).values(name="Louisiana")

        connection.execute(new_value)

        sel = select(State).where(State.name == "Louisiana").order_by(State.id)
        r = connection.execute(sel)
        state = r.fetchone()

        if (state is None):
            print("Not found")
        else:
            print("{}".format(state.id))
        connection.commit()
        connection.close()
