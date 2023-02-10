#!/usr/bin/python3
"""The review model"""

from .base_model import BaseModel


class Review(BaseModel):
    """The blueprint of a review"""

    place_id = ''

    user_id = ''

    text = ''
