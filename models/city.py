#!/usr/bin/python3
"""Defines a city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a City.
    Attributes:
        name (str): name of the city
        state_id (str): state of the city
    """
    state_id = ""
    name = ""
    