#!/usr/bin/env python3
"""
Module for filtering sensitive data in log messages, custom logging formatter,
and secure database connection using environment variables.
"""

import logging
import os
import re
import mysql.connector
from typing import List


# Fields considered as Personally Identifiable Information (PII)
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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
        return filter_datum(self.fields, self.REDACTION, original, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Create and return a logger named 'user_data' with INFO level,
    no propagation, and a StreamHandler with RedactingFormatter
    configured with PII_FIELDS.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.hasHandlers():
        stream_handler = logging.StreamHandler()
        formatter = RedactingFormatter(list(PII_FIELDS))
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to a secure MySQL database using credentials from environment variables.

    Environment Variables:
        PERSONAL_DATA_DB_USERNAME (default: "root")
        PERSONAL_DATA_DB_PASSWORD (default: "")
        PERSONAL_DATA_DB_HOST (default: "localhost")
        PERSONAL_DATA_DB_NAME (required)

    Returns:
        mysql.connector.connection.MySQLConnection: Database connection object.
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )
