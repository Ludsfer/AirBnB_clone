#!/usr/bin/python3
"""This file documents a Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """This implements a Place class."""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenities = []

    def __init__(self, *args, **kwargs):
        """Constructs a new Place instance."""
        super().__init__(*args, **kwargs)
