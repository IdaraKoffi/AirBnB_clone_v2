#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """State class to store state information"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
