#!/usr/bin/env python3
"""
Authentication module for managing user registration and password hashing.
"""

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.

    Args:
        password (str): The plain text password to hash.

    Returns:
        bytes: The salted, hashed password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initialize the Auth instance with a private DB instance."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with a hashed password.

        Args:
            email (str): The user's email.
            password (str): The user's plain password.

        Returns:
            User: The newly created user object.

        Raises:
            ValueError: If a user already exists with the given email.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            return self._db.add_user(email, hashed_pwd.decode("utf-8"))
