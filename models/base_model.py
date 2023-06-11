#!/usr/bin/python3
"""Base model for all models"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Base model class for all model classes"""
    def __init__(self):
        """class constructor"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """return human readable format for the object"""
        className = type(self).__name__
        objectID = self.id
        objAttributes = self.__dict__
        return "[{}] ({}) {}".format(className, objectID, objAttributes)

    def save(self):
        """Update the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of self.__dict__"""
        dictValue = self.__dict__.copy()
        created_at = self.created_at
        updated_at = self.updated_at
        dictValue['__class__'] = type(self).__name__
        dictValue['created_at'] = created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dictValue['updated_at'] = updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dictValue
