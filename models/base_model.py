#!/usr/bin/python3
"""The base model module"""
from uuid import uuid4

from datetime import datetime

from models import storage


class BaseModel:
    """The Base model class"""

    def __init__(self, *args, **kwargs):
        """The base class constructor"""

        if not kwargs:

            self.id = str(uuid4())

            self.created_at = datetime.now()

            self.updated_at = datetime.now()

            storage.new(self)

            return
        """Create attributes for kwargs"""
        ignored_attrs = ['created_at', '__class__', 'updated_at']

        self.created_at = datetime.fromisoformat(
            self.datevaluefor('created_at', kwargs['created_at']))

        self.updated_at = datetime.fromisoformat(
            self.datevaluefor('updated_at', kwargs['updated_at']))

        for k, v in kwargs.items():

            if k not in ignored_attrs:

                setattr(self, k, v)

    def datevaluefor(self, attr, value):
        """Validate the supplied value"""
        if not isinstance(value, str):
            raise TypeError("self.{attr} must be a string")
        if not value:
            raise ValueError("self.{attr} must not be empty")

        return value

    def __str__(self):
        """Returns the human representation string of a class object"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

        storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance"""

        d = self.__dict__.copy()

        d['__class__'] = self.__class__.__name__

        d['updated_at'] = self.updated_at.isoformat()

        d['created_at'] = self.created_at.isoformat()

        return d
