#!/usr/bin/python3
"""Defines a class Amenity that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """sub class that inherit from BaseModel.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """A new instance for Amenity
        """
        super().__init__(*args, **kwargs)
