#!/usr/bin/env python3
"""
Main file for testing user registration and valid login
"""
from auth import Auth

email = "bob@bob.com"
password = "MyPwdOfBob"

auth = Auth()

# Register the user
try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError:
    print("user already exists")

# Check valid login
if auth.valid_login(email, password):
    print("valid_login returns True on existing email with correct password")
else:
    print("valid_login returns False on existing email with correct password")
