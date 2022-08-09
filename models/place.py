#!/usr/bin/python3
"""Defines a place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a Place

    Attributes:
        city_id (str): city_id of the Place.
        user_id (str): user_id of the Place.
        name (str): name of the Place.
        description (str): description of the Place.
        number_rooms (int): number_rooms of the Place.
        number_bathrooms (int): number_bathrooms of the Place.
        max_guest (int): max_guest of the Place.
        price_by_night (int): price_by_night of the Place.
        latitude (float): latitude of the Place.
        longitude (float): longitude of the Place.
        amenity_ids (array): amenity_ids of the Place.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []