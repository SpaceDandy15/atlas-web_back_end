#!/usr/bin/env python3
"""
Flask app for user authentication service
"""

from flask import Flask, request, jsonify, abort, make_response, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()  # Exported as AUTH so 1-main.py can import it


@app.route('/sessions', methods=['POST'])
def login():
    """POST /sessions route to log in a user and set a session_id cookie."""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        abort(400)

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    if not session_id:
        abort(401)

    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """
    DELETE /sessions route to log out a user.
    Removes the session_id and redirects to GET /
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'])
def profile():
    """
    GET /profile route to get the user's email from a valid session.
    If session_id is invalid or user not found, abort with 403.
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    return jsonify({"email": user.email})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
