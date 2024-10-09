"""
This file contains the routes for the permission.
"""

from models.permission import Permission

from services.permission import (
    get_all_permissions,
    get_permission_by_id,
    create_permission,
    update_permission,
)


from fastapi import APIRouter

permission_router = APIRouter()


@permission_router.get("/")
def get_permissions():
    """
    This route gets all the permissions.

    Returns:
    - List[Permission]: A list of permissions.
    """
    return get_all_permissions()


@permission_router.get("/{id}")
def get_permission(permission_id: int):
    """
    This route gets a permission by id.

    Args:
    - permission_id (int): The id of the permission.

    Returns:
    - Permission: The permission.
    """
    return get_permission_by_id(permission_id)


@permission_router.post("/")
def post_permission(permission: Permission):
    """
    This route creates a permission.

    Args:
    - permission (Permission): The permission to create.

    Returns:
    - Permission: The created permission.
    """
    return create_permission(permission)


@permission_router.put("/{id}")
def put_permission(permission_id: int, permission: Permission):
    """
    This route updates a permission.

    Args:
    - permission_id (int): The id of the permission.
    - permission (Permission): The permission to update.

    Returns:
    - Permission: The updated permission.
    """
    return update_permission(permission_id, permission)
