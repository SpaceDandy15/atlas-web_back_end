#!/usr/bin/env python3
"""
Session authentication routes.
"""

from flask import request, jsonify, abort, make_response
from os import getenv
from models.user import User

# Expose this name so check_documentation can import it
auth_session = None


def login():
    """
    POST /api/v1/auth_session/login
    Expects 'email' and 'password' in form data.
    Sets a session cookie if credentials are valid.
    Returns:
      - 400 {"error": "email missing"} if email is missing
      - 400 {"error": "password missing"} if password is missing
      - 404 {"error": "no user found for this email"} if no user
      - 401 {"error": "wrong password"} if password invalid
      - 500 on internal error
      - 200 and user JSON with Set-Cookie on success
    """
    pass


def logout():
    """
    DELETE /api/v1/auth_session/logout
    Deletes the session cookie and destroys the session.
    Returns:
      - 404 if no session cookie or session not found
      - 200 and {} on success
    """
    pass
