#!/usr/bin/python3
"""Defines a city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a City

    Attributes:
        name (str): name of the city
        state_id (str): state_id of the city
    """
    state_id = ""
    name = ""
    