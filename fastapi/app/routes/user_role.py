"""
This file contains the routes for the user role.
"""

from models.user_role import UserRole

from services.user_role import (
    get_all_user_roles,
    get_user_role_by_id,
    create_user_role,
    update_user_role,
)


from fastapi import APIRouter

user_role_router = APIRouter()


@user_role_router.get("/")
def get_user_roles():
    """
    This route gets all the user roles.

    Returns:
    - List[UserRole]: A list of user roles.
    """
    return get_all_user_roles()


@user_role_router.get("/{id}")
def get_user_role(user_role_id: int):
    """
    This route gets a user role by id.

    Args:
    - user_role_id (int): The id of the user role.

    Returns:
    - UserRole: The user role.
    """
    return get_user_role_by_id(user_role_id)


@user_role_router.post("/")
def post_user_role(user_role: UserRole):
    """
    This route creates a user role.

    Args:
    - user_role (UserRole): The user role to create.

    Returns:
    - UserRole: The created user role.
    """
    return create_user_role(user_role)


@user_role_router.put("/{id}")
def put_user_role(user_role_id: int, user_role: UserRole):
    """
    This route updates a user role.

    Args:
    - user_role_id (int): The id of the user role.
    - user_role (UserRole): The user role to update.
    """
    return update_user_role(user_role_id, user_role)
