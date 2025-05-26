#!/usr/bin/env python3
"""
Session authentication module.
"""

import uuid
from models.user import User  # Import User model here


class SessionAuth:
    """
    SessionAuth class manages user sessions using session IDs.

    It stores session_id/user_id pairs in memory and provides methods to create
    sessions and retrieve user IDs from session IDs.
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a Session ID for a given user_id.

        Args:
            user_id (str): The user ID to create a session for.

        Returns:
            str or None: The session ID if user_id is valid, else None.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Return the User ID associated with a given Session ID.

        Args:
            session_id (str): The session ID.

        Returns:
            str or None: The user ID if session ID exists, else None.
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def session_cookie(self, request=None) -> str:
        """
        Retrieves the session cookie value from the request.

        Args:
            request: Flask request object.

        Returns:
            str or None: The value of the session cookie, or None if not found.
        """
        if request is None:
            return None

        session_name = " _my_session_id"  # or get from env/session_name variable
        # Better: session_name can be set as class attribute or retrieved from env

        # environment variable SESSION_NAME is set in the instructions

        from os import getenv
        session_name = getenv("SESSION_NAME", "_my_session_id")

        return request.cookies.get(session_name)

    def current_user(self, request=None) -> User:
        """
        Return the User instance based on the session cookie.

        Args:
            request: Flask request object.

        Returns:
            User instance if user found, else None.
        """
        if request is None:
            return None

        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        user = User.get(user_id)
        return user
