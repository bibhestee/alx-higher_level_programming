#!/usr/bin/python3
"""
    This script define a class of a City and an instance
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
        City - City class
        Attributes:
                    id = city id
                    name = city name
                    state_id = state id
                    __tablename__ = table name
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
