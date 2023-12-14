#!/usr/bin/python3
"""Defines a class City that inherits from BaseModel"""
from models.base_model import BaseModel

class City(BaseModel):

    state_id = ""
    name = ""
    """sub class that inherit from BaseModel
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)