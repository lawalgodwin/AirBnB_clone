#!/usr/bin/python3
"""The state model"""

from .base_model import BaseModel


class Place(BaseModel):
    """The blueprint of a place"""

    name = ''

    city_id = ''

    user_id = ''

    amenity_ids = list()

    description = ''

    number_rooms = 0

    number_bathrooms = 0

    max_guest = 0

    price_by_night = 0

    latitude = 0.0

    longitude = 0.0
