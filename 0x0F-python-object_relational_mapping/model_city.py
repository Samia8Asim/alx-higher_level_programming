#!/usr/bin/python3
"""file that contains the class definition of a City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    """
    city table class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    states_id = Column(Integer, nullable=False, ForeignKey("states.id"))
