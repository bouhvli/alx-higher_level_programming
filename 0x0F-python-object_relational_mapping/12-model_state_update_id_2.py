#!/usr/bin/python3
"""
this module has a script that update an object from db.
here we are using the sessionmaker.
"""
from sqlalchemy import create_engine, update
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

    upd = update(State).where(State.id == 2).values(name="New Mexico")

    session.execute(upd)
    session.commit()
    session.close()
