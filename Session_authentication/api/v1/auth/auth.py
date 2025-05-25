#!/usr/bin/env python3
"""
Auth module
"""

import os


class Auth:
    """
    Auth class to manage authentication and session cookies.
    """

    def session_cookie(self, request=None):
        """
        Retrieves the session cookie value from the Flask request.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            str or None: The value of the session cookie if present,
                         otherwise None.
        """
        if request is None:
            return None

        session_name = os.getenv("SESSION_NAME")
        if session_name is None:
            return None

        return request.cookies.get(session_name)
