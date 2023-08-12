#!/usr/bin/python3
import models
from datetime import datetime
import uuid
from models.__init__ import storage
"""
Basemodel class that defines all common
attributes/methods for other classes
"""


class BaseModel:
    "basemodel class defines common attributes"

    def __init__(self, *args, **kwargs):
        """
        initializes basemodel
        args:
            args: positional arguments
            kwarrgs: keyword ie (Key/value)  arguments
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        for_mat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, for_mat)
                else:
                    self.__dict__[key] = value
            else:
                models.storage.new(self)

    def __str__(self):
        """
        returns streing representation of the basemodel
        """
        x = self.__class__.__name__
        return "[{}] ({}) {}".format(x, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys
        /values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
