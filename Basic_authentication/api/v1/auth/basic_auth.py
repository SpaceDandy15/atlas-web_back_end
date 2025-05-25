#!/usr/bin/env python3
"""
Basic Authentication module.
Defines BasicAuth class to handle HTTP Basic Authentication.
"""

import base64
from typing import Tuple, TypeVar, Optional
from models.user import User
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic Authentication class that extends Auth.
    Provides methods to extract and decode Basic Authorization header,
    extract user credentials and return user object based on those credentials.
    """

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> Optional[str]:
        """
        Extract the Base64 part of the Authorization header.

        Args:
            authorization_header (str): The Authorization header string.

        Returns:
            Optional[str]: The Base64 encoded part of the header if valid.
        """
        if authorization_header is None or not isinstance(authorization_header,
                                                          str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(' ', 1)[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> Optional[str]:
        """
        Decode a Base64 encoded Authorization header.

        Args:
            base64_authorization_header (str): Base64 encoded string.

        Returns:
            Optional[str]: Decoded string in UTF-8 if valid, else None.
        """
        if base64_authorization_header is None or \
           not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[Optional[str], Optional[str]]:
        """
        Extract user email and password from the decoded Base64 header.

        Args:
            decoded_base64_authorization_header (str): Decoded Base64 string.

        Returns:
            Tuple[Optional[str], Optional[str]]: Tuple of (email, password),
            else (None, None).
        """
        if decoded_base64_authorization_header is None or \
           not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> Optional[TypeVar('User')]:
        """
        Retrieve a User instance based on email and password credentials.

        Args:
            user_email (str): User email.
            user_pwd (str): User password.

        Returns:
            Optional[User]: User instance if credentials match, else None.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        if not users:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> Optional[TypeVar('User')]:
        """
        Overload current_user to retrieve User instance from the request.

        Uses authorization header, extracts Base64 part, decodes it,
        extracts user credentials and finally returns the user object.

        Args:
            request (flask.Request, optional): Flask request object.

        Returns:
            Optional[User]: User instance if authentication succeeds.
        """
        authorization_header = self.authorization_header(request)
        base64_header = self.extract_base64_authorization_header(authorization_header)
        decoded_header = self.decode_base64_authorization_header(base64_header)
        user_email, user_pwd = self.extract_user_credentials(decoded_header)
        return self.user_object_from_credentials(user_email, user_pwd)
