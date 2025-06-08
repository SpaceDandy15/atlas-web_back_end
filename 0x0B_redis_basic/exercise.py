#!/usr/bin/env python3
"""Basic Redis caching module with call counting and call history"""

import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that counts how many times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs for a method.
    Inputs and outputs are stored in Redis lists named
    '<method_qualname>:inputs' and '<method_qualname>:outputs'.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        
        # Store the input args as string
        self._redis.rpush(input_key, str(args))
        
        # Call the actual method
        result = method(self, *args, **kwargs)
        
        # Store the output (result)
        self._redis.rpush(output_key, str(result))
        
        return result
    return wrapper


class Cache:
    """Cache class for storing and retrieving data in Redis"""

    def __init__(self):
        """Initialize Redis client and flush existing data"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @count_calls
    @call_history
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
