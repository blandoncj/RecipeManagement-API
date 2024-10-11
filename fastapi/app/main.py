"""
This module is the main module of the FastAPI application.
"""

from contextlib import asynccontextmanager
from config.database import database as connection
from routes.user_role import user_role_router
from routes.permission import permission_router
from routes.user import user_router
from fastapi import FastAPI
from fastapi.responses import RedirectResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    This function gets a connection from the database.
    """

    if connection.is_closed():
        connection.connect()
    try:
        yield
    finally:
        if not connection.is_closed():
            connection.close()


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    """
    This route redirects to the docs.
    """
    return RedirectResponse(url="/docs")


app.include_router(user_role_router, prefix="/api/user_roles", tags=["user_roles"])
app.include_router(permission_router, prefix="/api/permissions", tags=["permissions"])
app.include_router(user_router, prefix="/api/users", tags=["users"])
