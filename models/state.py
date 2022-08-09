#!/usr/bin/python3
"""Defines a state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a State

    Attributes:
        name (str): name of the state.
    """

    name = ""