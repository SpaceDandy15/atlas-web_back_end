#!/usr/bin/env python3
"""
Session authentication module.
"""

import uuid


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
