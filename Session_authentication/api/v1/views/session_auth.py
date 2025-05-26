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
    session_name = getenv(
        "HBNB_YELP_SESSION_NAME",
        getenv("SESSION_NAME", "_my_session_id")
    )
    response.set_cookie(session_name, session_id)
    return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """
    DELETE /api/v1/auth_session/logout
    Deletes the session cookie and destroys the session.

    Returns:
      - 404 if no session cookie or session not found
      - 200 and {} on success
    """
    # Import auth here to avoid circular import
    from api.v1.app import auth

    session_name = getenv(
        "HBNB_YELP_SESSION_NAME",
        getenv("SESSION_NAME", "_my_session_id")
    )
    session_id = request.cookies.get(session_name)
    if not session_id:
        abort(404)

    if not auth.destroy_session(request):
        abort(404)

    response = make_response(jsonify({}), 200)
    response.delete_cookie(session_name)
    return response
