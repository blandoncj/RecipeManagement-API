"""
This file contains the database configuration.
"""

from peewee import (
    Model,
    AutoField,
    CharField,
    IntegerField,
    BooleanField,
    MySQLDatabase,
)
from config.settings import DATABASE

database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    password=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)


class UserRoleModel(Model):
    """
    This class represents the user role model.
    """

    id = AutoField()
    name = CharField(max_length=30, unique=True, null=False)

    class Meta:
        """
        This class represents the metadata of the model
        """

        database = database
        table_name = "user_roles"


class PermissionModel(Model):
    """
    This class represents the permission model.
    """

    id = AutoField()
    name = CharField(max_length=30, unique=True, null=False)
    description = CharField(max_length=100, null=False)

    class Meta:
        """
        This class represents the metadata of the model
        """

        database = database
        table_name = "permissions"


class RolePermissionModel(Model):
    """
    This class represents the role permission model.
    """

    role_id = IntegerField(null=False)
    permission_id = CharField(max_length=30, unique=True, null=False)

    class Meta:
        """
        This class represents the metadata of the model
        """

        database = database
        table_name = "role_permissions"


class UserModel(Model):
    """
    This class represents the user model.
    """

    id = AutoField()
    username = CharField(max_length=30, unique=True, null=False)
    email = CharField(max_length=100, unique=True, null=False)
    password = CharField(max_length=255, null=False)
    account_type = CharField(max_length=30, null=False)
    profile_picture = CharField(max_length=255)
    role_id = IntegerField(null=False)
    is_active = BooleanField(default=True)

    class Meta:
        """
        This class represents the metadata of the model
        """

        database = database
        table_name = "users"
