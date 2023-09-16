#!/usr/bin/python3
"""
this module contains the class definition of a State
and an instance Base = declarative_base().
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base


class State(Base):
    """
    the class definition of the State that inherits the
    Base calss

    Attributes:
        id (int): id of the state.
        name (str): the name of the state.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    cities = relationship("City", backref="state", cascade="all, delete")
