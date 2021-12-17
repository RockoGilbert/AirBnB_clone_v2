#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship('City', cascade="all, delete, delete-orphan",
                              backref="state")
    else:
        @property
        def cities(self):
            """getter for cities list when using filestorage"""
            res = []
            for thing in models.storage.all(City).values():
                if thing.state_id == self.id:
                    res.append(thing)
            return res