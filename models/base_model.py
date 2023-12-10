#!/usr/bin/python3
"""
This file contains a class BaseModel that defines all
common attributes/methods for other classes.
"""
import uuid
import datetime as dt
from models import storage


class BaseModel:
    """
    This is a BaseModel class that defines all common
    attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Construct a new BaseModel instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value1 = dt.datetime.fromisoformat(value)
                        setattr(self, key, value1)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self) -> str:
        """
        This returns the string representation of the BaseModel instance
        in this format [<class name>] (<self.id>) <self.__dict__>
        """
        return f'[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>'

    def save(self) -> None:
        """
        This updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = dt.datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance.
        """
        tmp_dict = {'__class__': self.__class__.__name__}
        for k, v in self.__dict__.items():
            if k in ('created_at', 'updated_at'):
                v = v.isoformat()
            tmp_dict[k] = v
        return tmp_dict
