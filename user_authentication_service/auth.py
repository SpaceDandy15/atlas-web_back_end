#!/usr/bin/env python3
"""
auth.py - Authentication service
"""

import bcrypt
import uuid
from typing import Optional
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _generate_uuid() -> str:
    """Generate a new UUID and return its string representation."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """Hashes a password using bcrypt."""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.
        If user already exists, raise a ValueError.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_pw = self._hash_password(password)
            return self._db.add_user(email, hashed_pw)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user credentials.
        Returns True if password is correct for the given email.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str) -> Optional[str]:
        """
        Create a new session ID for a user identified by email.
        Return the session ID or None if user not found.
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self,
                                 session_id: Optional[str]) -> Optional[User]:
        """
        Retrieve a user based on a session ID.
        Args:
        session_id (str): The session ID to search for.
        Returns:
        User: The user with the given session ID, or None if not found.
        """
        if session_id is None:
            return None

        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroy a user's session by setting session_id to None.

        Args:
        user_id (int): user whose session is to be destroyed
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except Exception:
            pass
