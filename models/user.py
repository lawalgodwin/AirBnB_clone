#!/usr/bin/python3
"""The user module - this contains a class for defining a user"""

from .base_model import BaseModel


class User(BaseModel):
    """The blueprint for a user"""

    email = ''

    password = ''

    first_name = ''

    last_name = ''
