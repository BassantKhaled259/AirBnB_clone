#!/usr/bin/python3
"""Defines a class Base."""
import uuid
from datetime import datetime
import models

class BaseModel:
    """ Defines properties of Base """
    
    def __init__(self, *args, **kwargs):
        """ Create new instance """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for (key, value) in kwargs.item():
                if key in ('created_at', 'updated_at'):
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
                    
def __str__(self):
    """string represent of instance
    """
    return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"                
    
def save(self):
    """Update the public instance with current datetime.
    """
    self.updated_at = datetime.now()
    models.storage.save()

def to_dict(self):
    """Returns a dictionary contains all keys - values /
    in instance from __dict__ .
    """
    class_name = self.__class__.__name__
    self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
    self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
    self.__dict__["__class__"] = class_name
    return self.__dict__