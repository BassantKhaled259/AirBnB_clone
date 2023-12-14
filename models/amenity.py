#!/usr/bin/python3
"""Defines a class Amenity that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity sub-class that inherit from BaseModel. 
    """
    name = ""
   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)