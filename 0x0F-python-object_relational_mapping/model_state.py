#!/usr/bin/python3
"""
    This script define a class of a State and an instance
    Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        State - State class
        Attributes:
                    id = state id
                    name = state name
                    __tablename__ = table name
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
