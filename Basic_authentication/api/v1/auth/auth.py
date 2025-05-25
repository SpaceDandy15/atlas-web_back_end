#!/usr/bin/env python3
"""
Authentication module for the API
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """Template for all authentication systems"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        For now, always returns False.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from a request.
        For now, always returns None.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user.
        For now, always returns None.
        """
        return None
