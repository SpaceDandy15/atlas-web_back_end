#!/usr/bin/env python3
"""
Main file to test password encryption and validation
"""

hash_password = __import__('encrypt_password').hash_password
is_valid = __import__('encrypt_password').is_valid

password = "MyAmazingPassw0rd"
hashed = hash_password(password)

print("Hashed password:", hashed)

# Test valid password
print("Valid password check:", is_valid(hashed, password))

# Test invalid password
print("Invalid password check:", is_valid(hashed, "WrongPassword123"))
