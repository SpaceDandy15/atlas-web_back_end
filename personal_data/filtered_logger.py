#!/usr/bin/env python3
"""
Main script to read from users table and log filtered data
"""

import logging
import os
import mysql.connector
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates fields in a log message.
    """
    for field in fields:
        message = message.replace(f"{field}=", f"{field}={redaction}")
    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class for filtering PII fields
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Returns a configured logger object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger


def get_db():
    """
    Connect to the MySQL database using environment variables
    """
    return mysql.connector.connect(
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        database=os.getenv("PERSONAL_DATA_DB_NAME", "")
    )


def main():
    """
    Main function that connects to DB, fetches users, and logs filtered rows
    """
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()

    for row in cursor:
        row_str = "; ".join(f"{key}={value}" for key, value in row.items()) + ";"
        logger.info(row_str)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
