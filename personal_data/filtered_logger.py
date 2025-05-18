#!/usr/bin/env python3
"""
Filtering sensitive data in log messages and custom logging formatter.
"""

import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscate values of specified fields in a log message.

    Args:
        fields (List[str]): Fields to redact.
        redaction (str): String to replace field values.
        message (str): Log message.
        separator (str): Field separator.

    Returns:
        str: Log message with specified fields redacted.
    """
    pattern = (
        r'(' + '|'.join(fields) + r')=([^' + re.escape(separator) + r']*)'
    )
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """
    Logging formatter that redacts specified fields in log records.

    Attributes:
        REDACTION (str): The string used to replace sensitive data.
        FORMAT (str): The logging format string.
        SEPARATOR (str): The character that separates fields in log messages.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with fields to redact.

        Args:
            fields (List[str]): Fields whose values should be redacted.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, redacting specified fields.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log message with redactions applied.
        """
        original = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original,
                            self.SEPARATOR)
