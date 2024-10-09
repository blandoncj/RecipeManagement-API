"""
This file contains the functions for the user service.
"""

from config.database import UserModel
from models.user import User
from fastapi import Body, HTTPException


def get_all_users():
    """
    This function gets all the users.

    Returns:
    - List[User]: A list of users.
    """
    return list(UserModel.select().dicts())


def get_user_by_id(user_id: int):
    """
    This function gets a user by id.

    Args:
    - user_id (int): The id of the user.

    Returns:
    - User: The user.
    """
    try:
        return UserModel.get_by_id(user_id)
    except UserModel.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="User not found") from exc


def create_user(user: User = Body(...)):
    """
    This function creates a user.

    Args:
    - user (User): The user to create.

    Returns:
    - User: The created user.
    """

    try:
        return UserModel.create(**user.dict())
    except Exception as exc:
        raise HTTPException(status_code=400, detail="User already exists") from exc


def update_user(user_id: int, user: User = Body(...)):
    """
    This function updates a user.

    Args:
    - user_id (int): The id of the user.
    - user (User): The user to update.

    Returns:
    - User: The updated user.
    """

    try:
        user_model = UserModel.get_by_id(user_id)
        for key, value in user.dict().items():
            setattr(user_model, key, value)
        user_model.save()
        return user_model
    except UserModel.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="User not found") from exc
    except Exception as exc:
        raise HTTPException(status_code=400, detail="User already exists") from exc
