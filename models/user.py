#!/usr/bin/python3
"""This defines a User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """This implements a User class."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructs a User instance."""
        super().__init__(*args, **kwargs)
