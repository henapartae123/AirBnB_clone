#!/usr/bin/python3
"""Defines a amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent a Amenity
    
    Attributes:
        name (str): name of the amenity
    """

    name = ""
