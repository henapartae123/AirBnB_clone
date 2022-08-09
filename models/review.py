#!/usr/bin/python3
"""Defines a review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a Review

    Attributes:
        place_id (str): place_id of the Review
        user_id (str): user_id of the Review
        text (str): text of the Review
    """

    place_id = ""
    user_id = ""
    text = ""