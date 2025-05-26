#!/usr/bin/env python3
"""
API v1 views package initializer.
Defines the main blueprint and imports all submodules that
attach routes to it, before the blueprint is ever registered.
"""

from flask import Blueprint

# Create the main blueprint for /api/v1
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all view modules here so their @app_views.route decorators run immediately
# **Order matters**: these imports must come before the blueprint is registered in app.py

# Standard index routes (status, stats, unauthorized, forbidden)
from api.v1.views.index import status, stats, unauthorized, forbidden

# User management routes (GET/POST/PUT/DELETE /users)
from api.v1.views.users import (
    view_all_users,
    view_one_user,
    create_user,
    update_user,
    delete_user
)

# Session auth routes (login, logout)
from api.v1.views.session_auth import login, logout
