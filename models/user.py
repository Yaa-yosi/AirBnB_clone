#!/usr/bon/python3
"""Module creates User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """class for managing user data"""

    def __init__(self, *args, **kwargs):
        """Initializes a User Class"""

        super().__init__(*args, **kwargs)

        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

