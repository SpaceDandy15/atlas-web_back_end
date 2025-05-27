#!/usr/bin/env python3
"""
This module defines a SQLAlchemy model for the 'users' table,
used for managing user authentication data including credentials
and session information.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy User model for the 'users' table. This model stores
    user credentials, session information, and password reset tokens.
    """

    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: str = Column(String(250), nullable=True)
    reset_token: str = Column(String(250), nullable=True)
