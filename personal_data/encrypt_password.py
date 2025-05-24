#!/usr/bin/env python3
"""
Encrypt password module
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt and return the salted hash.

    Args:
        password (str): The password string to hash.

    Returns:
        bytes: The salted, hashed password.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
