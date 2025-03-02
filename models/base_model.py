#!/usr/bin/python3
"""Base model for all models"""
from datetime import datetime
from . import storage
from uuid import uuid4


class BaseModel:
    """Base model class for all model classes"""
    def __init__(self, *args, **kwargs):
        """class constructor"""
        if kwargs and kwargs != {}:
            # remove the class attribute
            del kwargs['__class__']
            dictValue = kwargs.copy()
            for k, v in dictValue.items():
                setattr(self, k, v)
            # change the string formatted datetime to datetime object
            created_at = self.created_at
            updated_at = self.updated_at
            self.created_at = datetime.strptime(
                    created_at,
                    "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(
                    updated_at,
                    "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """return human readable format for the object"""
        className = type(self).__name__
        objectID = self.id
        objAttributes = self.__dict__
        return "[{}] ({}) {}".format(className, objectID, objAttributes)

    def save(self):
        """Update the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of self.__dict__"""
        dictValue = self.__dict__.copy()
        created_at = self.created_at
        updated_at = self.updated_at
        dictValue['__class__'] = type(self).__name__
        dictValue['created_at'] = created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dictValue['updated_at'] = updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dictValue
