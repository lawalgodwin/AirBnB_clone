#!/usr/bin/python3
"""The city model"""

from .base_model import BaseModel


class City(BaseModel):
    """The blueprint of a city"""

    state_id = ''

    name = ''
