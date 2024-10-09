"""
This file contains the model for the user role.
"""

from pydantic import BaseModel, Field


class UserRole(BaseModel):
    """
    This class represents the user role model.
    """

    name: str = Field(
        ..., example="Admin", description="The name of the user role.", max_length=30
    )
    description: str = Field(
        ...,
        example="The admin user role.",
        description="The description of the user role.",
        max_length=100,
    )

    class Config:
        """
        strips leading/trailing whitespace
        """

        anystr_strip_whitespace = True
