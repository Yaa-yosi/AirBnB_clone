#!/usr/bin/python3
"""Amenity Module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    The public class attribute should return an empty string
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = ""

