#!/usr/bin/python3
"""City Module"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    The public class attributes should be empty
    """

    def __init__(self, *args, **kwargs):
        """Initializes City class"""

        super().__init__(*args, **kwargs)

        self.state_id = ""
        self.name = ""

