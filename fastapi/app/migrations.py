"""
This file contains the database migrations 
"""

from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    Enum,
    ForeignKey,
    Integer,
    String,
    Date,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from config.settings import DATABASE

Base = declarative_base()


class UserRole(Base):
    """
    User roles table
    """

    __tablename__ = "user_roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=True, nullable=False)

    # relationship
    permissions = relationship("RolePermission", back_populates="role")
    users = relationship("User", back_populates="role")


class Permission(Base):
    """
    Permissions table
    """

    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=True, nullable=False)
    description = Column(String(100), nullable=True)

    # relationship
    roles = relationship("RolePermission", back_populates="permission")


class RolePermission(Base):
    """
    Role permissions table
    """

    __tablename__ = "role_permissions"
    role_id = Column(
        Integer, ForeignKey("user_roles.id"), primary_key=True, nullable=False
    )
    permission_id = Column(
        Integer, ForeignKey("permissions.id"), primary_key=True, nullable=False
    )

    # relationship
    role = relationship("UserRole", back_populates="permissions")
    permission = relationship("Permission", back_populates="roles")


class User(Base):
    """
    Users table
    """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    account_type = Column(String(30), nullable=False)
    profile_picture = Column(String(255), nullable=False)
    role_id = Column(Integer, ForeignKey("user_roles.id"), nullable=False)
    is_active = Column(Boolean, default=True)

    # relationship
    role = relationship("UserRole", back_populates="users")
    families = relationship("UserFamily", back_populates="user")
    inventories = relationship("InventoryIngredient", back_populates="user")
    recipes = relationship("Recipe", back_populates="user")
    menus = relationship("Menu", back_populates="user")
    shopping_lists = relationship("ShoppingList", back_populates="user")


class Family(Base):
    """
    Families table
    """

    __tablename__ = "families"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=True, nullable=False)

    # relationship
    users = relationship("UserFamily", back_populates="family")


class UserFamily(Base):
    """
    User families table
    """

    __tablename__ = "user_families"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True, nullable=False)
    family_id = Column(
        Integer, ForeignKey("families.id"), primary_key=True, nullable=False
    )

    # relationship
    user = relationship("User", back_populates="families")
    family = relationship("Family", back_populates="users")


class Unit(Base):
    """
    Units table
    """

    __tablename__ = "units"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)

    # relationship
    ingredients = relationship("Ingredient", back_populates="unit")


class IngredientCategory(Base):
    """
    Ingredient categories table
    """

    __tablename__ = "ingredient_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)

    # relationship
    ingredients = relationship("Ingredient", back_populates="category")


class Ingredient(Base):
    """
    Ingredients table
    """

    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=True, nullable=False)
    calories = Column(Integer, nullable=False)
    expiration_date = Column(Date, nullable=False)
    is_active = Column(Boolean, default=True)
    category_id = Column(
        Integer, ForeignKey("ingredient_categories.id"), nullable=False
    )
    unit_id = Column(Integer, ForeignKey("units.id"), nullable=False)

    # relationship
    category = relationship("IngredientCategory", back_populates="ingredients")
    unit = relationship("Unit", back_populates="ingredients")
    inventories = relationship("InventoryIngredient", back_populates="ingredient")
    recipes = relationship("RecipeIngredient", back_populates="ingredient")
    shopping_lists = relationship("ShoppingListIngredient", back_populates="ingredient")


class InventoryIngredient(Base):
    """
    Inventory ingredients table
    """

    __tablename__ = "inventory_ingredients"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True, nullable=False)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    # relationship
    ingredient = relationship("Ingredient", back_populates="inventories")
    user = relationship("User", back_populates="inventories")


class RecipeCategory(Base):
    """
    Recipe categories table
    """

    __tablename__ = "recipe_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)

    # relationship
    recipes = relationship("RecipeCategories", back_populates="category")


class Recipe(Base):
    """
    Recipes table
    """

    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=True, nullable=False)
    description = Column(String(100), nullable=False)
    instructions = Column(String(255), nullable=False)
    preparation_time = Column(Integer, nullable=False)
    difficulty = Column(Integer, nullable=False)
    is_public = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # relationship
    user = relationship("User", back_populates="recipes")
    categories = relationship("RecipeCategories", back_populates="recipe")
    ingredients = relationship("RecipeIngredient", back_populates="recipe")
    menus = relationship("MenuRecipe", back_populates="recipe")


class RecipeCategories(Base):
    """
    Recipe categories table
    """

    __tablename__ = "recipe_categories"
    recipe_id = Column(
        Integer, ForeignKey("recipes.id"), primary_key=True, nullable=False
    )
    category_id = Column(
        Integer, ForeignKey("recipe_categories.id"), primary_key=True, nullable=False
    )

    # relationship
    recipe = relationship("Recipe", back_populates="categories")
    category = relationship("RecipeCategory", back_populates="recipes")


class RecipeIngredient(Base):
    """
    Recipe ingredients table
    """

    __tablename__ = "recipe_ingredients"
    recipe_id = Column(
        Integer, ForeignKey("recipes.id"), primary_key=True, nullable=False
    )
    ingredient_id = Column(
        Integer, ForeignKey("ingredients.id"), primary_key=True, nullable=False
    )
    quantity = Column(Integer, nullable=False)

    # relationship
    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="recipes")


class Menu(Base):
    """
    Menus table
    """

    __tablename__ = "menus"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=True, nullable=False)
    menu_date = Column(Date, nullable=False)
    meal_type = Column(Enum("Breakfast", "Lunch", "Dinner"), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(Date, nullable=False, default=datetime.now())
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # relationship
    user = relationship("User", back_populates="menus")
    recipes = relationship("MenuRecipe", back_populates="menu")


class MenuRecipe(Base):
    """
    Menu recipes table
    """

    __tablename__ = "menu_recipes"
    menu_id = Column(Integer, ForeignKey("menus.id"), primary_key=True, nullable=False)
    recipe_id = Column(
        Integer, ForeignKey("recipes.id"), primary_key=True, nullable=False
    )

    # relationship
    menu = relationship("Menu", back_populates="recipes")
    recipe = relationship("Recipe", back_populates="menus")


class ShoppingList(Base):
    """
    Shopping lists table
    """

    __tablename__ = "shopping_lists"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.now())

    # relationship
    user = relationship("User", back_populates="shopping_lists")
    ingredients = relationship("ShoppingListIngredient", back_populates="shopping_list")


class ShoppingListIngredient(Base):
    """
    Shopping list ingredients table
    """

    __tablename__ = "shopping_list_ingredients"
    shopping_list_id = Column(
        Integer, ForeignKey("shopping_lists.id"), primary_key=True, nullable=False
    )
    ingredient_id = Column(
        Integer, ForeignKey("ingredients.id"), primary_key=True, nullable=False
    )
    quantity = Column(Integer, nullable=False)
    bought = Column(Boolean, default=False)

    # relationship
    shopping_list = relationship("ShoppingList", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="shopping_lists")


# config database
user_info = f"{DATABASE['user']}:{DATABASE['password']}"
host_info = f"{DATABASE['host']}/{DATABASE['name']}"

DATABASE_URL = f"mysql+pymysql://{user_info}@{host_info}"

engine = create_engine(DATABASE_URL)

# create a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
