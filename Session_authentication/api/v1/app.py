#!/usr/bin/env python3
"""
Route module for the API.
Sets up the Flask application and authentication handling.
"""
from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = getenv("AUTH_TYPE")

if auth_type == "auth":
    # Generic token-based auth
    from api.v1.auth.auth import Auth
    auth = Auth()
elif auth_type == "basic_auth":
    # HTTP Basic Auth
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == "session_auth":
    # Session based auth with cookies
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status() -> tuple[str, int]:
    """Simple status route returning plain OK"""
    return "OK", 200


@app.before_request
def before_request_func():
    """
    Intercepts incoming requests before routing.
    Checks if the request requires authentication and validates the
    presence of valid authorization headers and authenticated users.
    Aborts with appropriate HTTP error codes if authentication fails.
    """
    if auth is None:
        return

    excluded_paths = [
        '/api/v1/status',
        '/api/v1/status/',
        '/api/v1/unauthorized',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden',
        '/api/v1/forbidden/',
        '/api/v1/auth_session/login',
        '/api/v1/auth_session/login/'
    ]

    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None and auth.session_cookie(request) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)


@app.errorhandler(404)
def not_found(error):
    """Handles 404 Not Found errors"""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized_error(error):
    """Handles 401 Unauthorized errors"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error):
    """Handles 403 Forbidden errors"""
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port)
