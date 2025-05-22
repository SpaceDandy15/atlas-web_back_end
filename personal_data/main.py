#!/usr/bin/env python3
"""
Main file to test get_db and logger setup.
"""

from filtered_logger import get_db, get_logger

# Test database connection
def test_db():
    print("Connecting to DB and querying user count...")
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users;")
    for row in cursor:
        print("User count:", row[0])
    cursor.close()
    db.close()

# Test logger
def test_logger():
    print("Testing logger output with PII redaction...")
    logger = get_logger()
    log_msg = "name=John Doe; email=john@example.com; phone=123-456-7890; ssn=111-22-3333; password=secret123;"
    logger.info(log_msg)

if __name__ == "__main__":
    test_db()
    test_logger()
