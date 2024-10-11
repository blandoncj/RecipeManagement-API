"""
API key Authentication
"""

import os

from dotenv import load_dotenv
from fastapi import HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "x-api-key"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(api_key: str = Security(api_key_header)):
    """
    Validates the provided API key from the request header.

    Args:
        api_key_header (str): The API key obtained from the `x-api-key` header.

    Returns:
        str: The API key if it is valid.

    Raises:
        HTTPException: If the API key is invalid or missing, an HTTP exception
        with status 403 (Forbidden) and an "Unauthorized" message is raised.
    """
    if api_key == API_KEY:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail={
            "status": False,
            "status_code": status.HTTP_403_FORBIDDEN,
            "message": "Unauthorized",
        },
    )
