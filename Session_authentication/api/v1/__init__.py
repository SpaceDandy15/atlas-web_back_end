#!/usr/bin/env python3
"""
API v1 views package initializer.
Sets up the main blueprint and registers all sub-blueprints (including session_auth).
"""

from flask import Blueprint

# Create main blueprint for API v1
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import and register session_auth blueprint
from api.v1.views.session_auth import auth_session

app_views.register_blueprint(auth_session)
