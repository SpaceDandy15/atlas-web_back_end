#!/usr/bin/env python3
"""
Session authentication routes.
"""

from os import getenv
from flask import request, jsonify, abort, make_response
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def login():
    """
    POST /api/v1/auth_session/login
    - Expects 'email' and 'password' in form data.
    - On success, returns user.to_json() and sets a session cookie.
    - Errors:
        * 400 {"error": "email missing"} if email is missing
        * 400 {"error": "password missing"} if password is missing
        * 404 {"error": "no user found for this email"} if no user
        * 401 {"error": "wrong password"} if password invalid
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Import auth here to avoid circular import
    from api.v1.app import auth

    session_id = auth.create_session(user.id)
    if not session_id:
        abort(500)

    response = make_response(jsonify(user.to_json()), 200)
    session_name = getenv('SESSION_NAME', '_my_session_id')
    response.set_cookie(session_name, session_id)
    return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """
    DELETE /api/v1/auth_session/logout
    - Reads the session cookie, destroys the session, and clears the cookie.
    - Errors:
        * 404 if no session cookie or session not found
    - Success:
        * {} with status 200
    """
    # Import auth here to avoid circular import
    from api.v1.app import auth

    if not auth.destroy_session(request):
        abort(404)

    return jsonify({}), 200
