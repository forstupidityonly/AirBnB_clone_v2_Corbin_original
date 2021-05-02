#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import String, Integer, ForeignKey, Column
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City

storage_type = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")

    else:
        @property
        def cities():
            """[This is a getter that]
            Returns:
                [list]: [list of cities]
            """
            new_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    new_list.append(city)
            return new_list
