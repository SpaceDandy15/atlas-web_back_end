#!/usr/bin/env python3
"""
Authentication module for password hashing
"""

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
