"""
This file contains the model for the permission.
"""

from pydantic import BaseModel, Field


class Permission(BaseModel):
    """
    This class represents the permission model.
    """

    name: str = Field(
        ...,
        example="Create Recipe",
        description="The name of the permission.",
        max_length=30,
    )
    description: str = Field(
        ...,
        example="The create recipe permission.",
        description="The description of the permission.",
        max_length=100,
    )

    class Config:
        """
        strips leading/trailing whitespace
        """

        anystr_strip_whitespace = True
