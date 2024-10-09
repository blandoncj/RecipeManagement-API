"""
This file contains the routes for the user.
"""

from models.user import User

from services.user import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
)


from fastapi import APIRouter

user_router = APIRouter()


@user_router.get("/")
def get_users():
    """
    This route gets all the users.

    Returns:
    - List[User]: A list of users.
    """
    return get_all_users()


@user_router.get("/{id}")
def get_user(user_id: int):
    """
    This route gets a user by id.

    Args:
    - user_id (int): The id of the user.

    Returns:
    - User: The user.
    """
    return get_user_by_id(user_id)


@user_router.post("/")
def post_user(user: User):
    """
    This route creates a user.

    Args:
    - user (User): The user to create.

    Returns:
    - User: The created user.
    """
    return create_user(user)


@user_router.put("/{id}")
def put_user(user_id: int, user: User):
    """
    This route updates a user.

    Args:
    - user_id (int): The id of the user.
    - user (User): The user to update.
    """
    return update_user(user_id, user)
