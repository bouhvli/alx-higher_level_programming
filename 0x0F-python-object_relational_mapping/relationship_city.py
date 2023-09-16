#!/usr/bin/python3
"""
this module contains the class definition of a City
and an instance Base = declarative_base().
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """
      the class definition of the City that inherits the
      Base calss

      Attributes:
          id (int): id of the city.
          name (str): the name of the city.
          state_id (int): id of the state as foreign key
      """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
