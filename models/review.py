#!/usr/bin/python3
"""Defines a class Review  that inherits from BaseModel"""
from models.base_model import BaseModel


class Review (BaseModel):
    """Class that defines properties of Review .
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
