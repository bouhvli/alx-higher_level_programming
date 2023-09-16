#!/usr/bin/python3
"""
this module has a script that deletes all the objects with a name
containing the letter 'a' from the database"""
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


if __name__ == '__main__':
    meta = Base.metadata

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    upd = delete(State).where(State.name.ilike("%a%"))

    session.execute(upd)
    session.commit()
    session.close()
