#!/usr/bin/python3
"""This documents a state class."""
from models.base_model import BaseModel


class State(BaseModel):
    """This implements State class."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructs a State instance."""
        super().__init__(*args, **kwargs)
