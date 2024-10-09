"""
This file contains the functions for the user role service.
"""

from config.database import UserRoleModel
from models.user_role import UserRole
from fastapi import Body, HTTPException


def get_all_user_roles():
    """
    This function gets all the user roles.

    Returns:
    - List[UserRole]: A list of user roles.
    """
    return list(UserRoleModel.select().dicts())


def get_user_role_by_id(user_role_id: int):
    """
    This function gets a user role by id.

    Args:
    - user_role_id (int): The id of the user role.

    Returns:
    - UserRole: The user role.
    """
    try:
        return UserRoleModel.get_by_id(user_role_id)
    except UserRoleModel.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="User role not found") from exc


def create_user_role(user_role: UserRole = Body(...)):
    """
    This function creates a user role.

    Args:
    - user_role (UserRole): The user role to create.

    Returns:
    - UserRole: The created user role.
    """

    try:
        return UserRoleModel.create(**user_role.dict())
    except Exception as exc:
        raise HTTPException(status_code=400, detail="User role already exists") from exc


def update_user_role(user_role_id: int, user_role: UserRole = Body(...)):
    """
    This function updates a user role.

    Args:
    - user_role_id (int): The id of the user role.
    - user_role (UserRole): The user role to update.

    Returns:
    - UserRole: The updated user role.
    """
    try:
        user_role_model = UserRoleModel.get_by_id(user_role_id)
        for key, value in user_role.dict().items():
            setattr(user_role_model, key, value)
        user_role_model.save()
        return user_role_model
    except UserRoleModel.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="User role not found") from exc
    except Exception as exc:
        raise HTTPException(status_code=400, detail="User role already exists") from exc
