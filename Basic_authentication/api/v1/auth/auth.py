#!/usr/bin/env python3
"""
Authentication module
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class for managing the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if authentication is required for the given path"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        # Ensure path ends with slash for comparison
        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/') and path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Returns the Authorization header from a request"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None - to be implemented later"""
        return None
