#!/usr/bin/env python3
"""
DB module for interacting with the User database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.session import Session
from user import Base, User


class DB:
    """DB class for managing the SQLAlchemy session and user operations"""

    def __init__(self) -> None:
        """Initialize a new database connection and session"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Return a memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find the first user matching the given criteria"""
        if not kwargs:
            raise InvalidRequestError("No search arguments provided")

        try:
            return self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("No user found")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid query arguments")

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user attributes by ID with provided values"""
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(f"Invalid attribute: {key}")
            setattr(user, key, value)

        self._session.commit()
