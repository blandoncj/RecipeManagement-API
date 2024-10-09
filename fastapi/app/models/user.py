"""
This file contains the model for the user.
"""

from pydantic import BaseModel, Field


class User(BaseModel):
    """
    This class represents the user model.
    """

    username: str = Field(
        ..., example="johndoe", description="The username of the user.", max_length=30
    )
    email: str = Field(
        ...,
        example="johndoe@gmail.com",
        description="The email of the user.",
        max_length=100,
    )
    password: str = Field(
        ..., example="password", description="The password of the user.", max_length=255
    )

    account_type: str = Field(
        ..., example="admin", description="The account type of the user.", max_length=30
    )

    profile_picture: str = Field(
        ...,
        example="profile.jpg",
        description="The profile picture of the user.",
        max_length=255,
    )

    role_id: int = Field(..., example=1, description="The role id of the user.")

    is_active: bool = Field(..., example=True, description="The status of the user.")

    class Config:
        """
        strips leading/trailing whitespace
        """

        anystr_strip_whitespace = True
