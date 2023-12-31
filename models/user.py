#!/usr/bin/python3
"""Defines a class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """ sub class that inherit from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
