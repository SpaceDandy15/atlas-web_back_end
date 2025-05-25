#!/usr/bin/env python3
"""
BasicAuth module for handling Basic Authentication
"""
from api.v1.auth.auth import Auth
import base64
import binascii


class BasicAuth(Auth):
    """
    BasicAuth inherits from Auth for handling Basic Authentication logic
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the Base64 part from the Authorization header for Basic Auth.

        Args:
            authorization_header (str): The full Authorization header.

        Returns:
            str: The Base64 encoded credentials or None.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ", 1)[1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64 encoded authorization header.

        Args:
            base64_authorization_header (str): Base64 encoded credentials.

        Returns:
            str: Decoded string in UTF-8 or None.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            decoded_bytes = base64.b64decode(base64_bytes)
            return decoded_bytes.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts the user email and password from the decoded Base64 header.

        Args:
            decoded_base64_authorization_header (str): Decoded Base64 string.

        Returns:
            tuple: (user_email, user_password) or (None, None)
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password
