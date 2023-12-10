#!/usr/bin/python3
"""This documents amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Definition of Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constuct a new Amenity instance."""
        super().__init__(*args, **kwargs)
