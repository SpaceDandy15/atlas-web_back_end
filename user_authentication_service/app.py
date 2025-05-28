#!/usr/bin/env python3
"""
Flask app for user authentication service
"""

from flask import Flask, request, jsonify, abort, make_response
from auth import Auth

app = Flask(__name__)
AUTH = Auth()  # Exported as AUTH so 0-main.py can import it


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
