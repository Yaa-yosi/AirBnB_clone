#!/usr/bin/python3
"""State Module"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    All attributes should be empty
    """

    def __init__(self, *args, **kwargs):
        """Initializes a State class"""

        super().__init__(*args, **kwargs)

        self.name = ""

