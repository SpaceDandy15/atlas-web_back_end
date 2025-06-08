#!/usr/bin/env python3
"""Basic Redis caching module"""

import redis
import uuid
from typing import Union


class Cache:
    """Cache class for storing data in Redis"""

    def __init__(self):
        """Initialize Redis client and flush existing data"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis with a randomly generated key.

        Args:
            data: The data to store (str, bytes, int, or float)

        Returns:
            str: The key used to store the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
