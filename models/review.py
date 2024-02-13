#!/usr/bin/python3
"""Review Module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    All attrbutes should be empty
    """

    def __init__(self, *args, **kwargs):
        """Initializes a Review Class"""

        super().__init__(*args, **kwargs)

        self.place_id = ""
        self.user_id = ""
        self.text = ""

