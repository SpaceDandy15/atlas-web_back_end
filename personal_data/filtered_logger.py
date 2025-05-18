#!/usr/bin/env python3
"""
Module for filtering sensitive data in log messages.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscate fields in a log message.

    Args:
        fields (List[str]): Fields to redact.
        redaction (str): String to replace field values.
        message (str): Log message.
        separator (str): Field separator.

    Returns:
        str: Obfuscated log message.
    """
    pattern = (
        r'(' + '|'.join(fields) + r')=([^' + re.escape(separator) + r']*)'
    )
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
