#!/usr/bin/python3
"""[This is a storage engine that stores class
    attributes in a database]
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """[This is the strorage class]
    """
    __engine = None
    __session = None

    def __init__(self):
        """[This instantiates the variable]
        """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        current_host = getenv('HBNB_MYSQL_HOST')
        database_name = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, current_host, database_name, pool_pre_ping=True))
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all objects depending of the class name"""
# Come back to this
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                }
        my_dict = {}
        for itr in classes:
            if cls is None or cls == itr:
                objs = self.__session.query(classes[itr])
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    my_dict[key] = obj
        return my_dict

    def new(self, obj):
        """ This adds the object to
            to the current database session
        """
        if obj is not None:
            self.__session.add(obj)
            self.save()

    def save(self):
        """commit all changes of the
            current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current
            database session obj if not None
        """
        if obj is not None:
            del obj
            self.save()

    def reload(self):
        """ This creates all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """method on the private session attribute"""
        self.__session.close()