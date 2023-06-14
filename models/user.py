#!/usr/bin/python3
"""The user model"""
from models.base_model import BaseModel


class User(BaseModel):
    """The User class definition"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
