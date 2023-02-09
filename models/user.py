#!/usr/bin/python3
"""
class user inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    representation of user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        init method of user
        """
        super().__init__(*args, **kwargs)
