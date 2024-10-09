"""
This file contains the functions for the permission service.
"""

from config.database import PermissionModel
from models.permission import Permission
from fastapi import Body, HTTPException


def get_all_permissions():
    """
    This function gets all the permissions.

    Returns:
    - List[Permission]: A list of permissions.
    """
    return list(PermissionModel.select().dicts())


def get_permission_by_id(permission_id: int):
    """
    This function gets a permission by id.

    Args:
    - permission_id (int): The id of the permission.

    Returns:
    - Permission: The permission.
    """
    try:
        return PermissionModel.get_by_id(permission_id)
    except PermissionModel.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Permission not found") from exc


def create_permission(permission: Permission = Body(...)):
    """
    This function creates a permission.

    Args:
    - permission (Permission): The permission to create.

    Returns:
    - Permission: The created permission.
    """

    try:
        return PermissionModel.create(**permission.dict())
    except Exception as exc:
        raise HTTPException(
            status_code=400, detail="Permission already exists"
        ) from exc


def update_permission(permission_id: int, permission: Permission = Body(...)):
    """
    This function updates a permission.

    Args:
    - permission_id (int): The id of the permission.
    - permission (Permission): The permission to update.

    Returns:
    - Permission: The updated permission.
    """
    try:
        permission_model = PermissionModel.get_by_id(permission_id)
        for key, value in permission.dict().items():
            setattr(permission_model, key, value)
        permission_model.save()
        return permission_model
    except PermissionModel.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Permission not found") from exc
