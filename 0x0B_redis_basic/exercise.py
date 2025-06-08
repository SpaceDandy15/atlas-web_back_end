#!/usr/bin/env python3
"""Basic Redis caching module with call counting"""

import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method is called.

    Uses Redis key based on the method's __qualname__.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """Cache class for storing and retrieving data in Redis"""

    def __init__(self):
        """Initialize Redis client and flush existing data"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Retrieve data from Redis and optionally convert it using a callable.

        Args:
            key (str): The Redis key.
            fn (Optional[Callable]): A callable to convert the retrieved data.

        Returns:
            Any: The retrieved (and possibly converted) data, or None if key does not exist.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value
