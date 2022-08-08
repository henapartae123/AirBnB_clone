#!/usr/bin/python3
"""Defines BaseModel class"""
import uuid
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """the BaseModel class"""

    def __init__(self, *args, **kwargs):
        
        """Initailizes the BaseModel class

        Args:
            *args (any): Unused
        
        
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        forma = "%Y-%m-%dT%H:%M:%S.%f"
    
    def save(self):

        """Update updated_at with the current datetime."""
        
        self.updated_at = datetime.today()
        models.storage.save()
    
    def to_dict(self):

        """Return the dictionary of the BaseModel instance"""

        dict = self.__dict__.copy()
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        dict["__class__"] = self.__class__.__name__
        return dict
        