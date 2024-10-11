from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from config.settings import DATABASE

Base = declarative_base()


class UserRole(Base):
    __tablename__ = "user_roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=True, nullable=False)


class Permission(Base):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=True, nullable=False)
    description = Column(String(100), nullable=True)


class RolePermission(Base):
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


class Family(Base):
    __tablename__ = "families"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=True, nullable=False)


# config database
DATABASE_URL = f"mysql+pymysql://{DATABASE['user']}:{DATABASE['password']}@{DATABASE['host']}/{DATABASE['name']}"
engine = create_engine(DATABASE_URL)


# create a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
