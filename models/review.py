#!/usr/bin/python3
"""This file documents a review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """This implements a Review class."""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Constructs a Review class"""
        super().__init__(*args, **kwargs)
