#!/usr/bin/env python3
"""Basic Redis caching module"""

import redis
import uuid
from typing import Union, Callable, Optional, Any


class Cache:
    """Cache class for storing and retrieving data in Redis"""

    def __init__(self):
        """Initialize Redis client and flush existing data"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis with a randomly generated key.

        Args:
            data: The data to store

        Returns:
            str: The key used to store the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Args:
            key: Redis key to retrieve
            fn: Optional function to convert the result

        Returns:
            The retrieved (and possibly converted) value, or None if key doesn't exist
        """
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

    def get_str(self, key: str) -> str:
        """
        Retrieve data from Redis and decode as UTF-8 string.

        Args:
            key: Redis key to retrieve

        Returns:
            Decoded string
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve data from Redis and convert to integer.

        Args:
            key: Redis key to retrieve

        Returns:
            Integer value
        """
        return self.get(key, fn=int)
