#!/usr/bin/env python3
"""
Session authentication routes.
"""

from os import getenv
from flask import Blueprint, request, jsonify, abort, make_response
from models.user import User
from api.v1.auth.session_auth import SessionAuth
from flask import abort, jsonify, request
from api.v1.app import auth


auth_session = Blueprint('auth_session', __name__)
session_auth = SessionAuth()


@auth_session.route('/api/v1/auth_session/login', methods=['POST'],
                    strict_slashes=False)
def login():
    """
    Login route to create a session for valid user credentials.

    Expects 'email' and 'password' form data.
    Sets a session cookie if credentials are valid.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = session_auth.create_session(user.id)
    if not session_id:
        abort(500)

    response = jsonify(user.to_dict())
    session_name = getenv('SESSION_NAME', '_my_session_id')
    response.set_cookie(session_name, session_id)
    return response


@auth_session.route('/api/v1/auth_session/logout', methods=['DELETE'],
                    strict_slashes=False)
def logout():
    """
    Logout route to destroy the user session.

    Deletes the session cookie and destroys the session.
    """
    session_name = getenv('SESSION_NAME', '_my_session_id')
    session_id = request.cookies.get(session_name)

    if not session_id:
        abort(404)

    success = session_auth.destroy_session(session_id)
    if not success:
        abort(404)

    response = make_response(jsonify({}), 200)
    response.delete_cookie(session_name)
    return response

@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """ Deletes the session / logs out the user """
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200