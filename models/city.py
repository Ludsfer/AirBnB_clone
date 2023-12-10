#!/usr/bin/python3
"""This documents a city class."""
from models.base_model import BaseModel


class City(BaseModel):
    """This is an implementation of City class."""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructs a new City instance."""
        super().__init__(*args, **kwargs)
