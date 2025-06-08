#!/usr/bin/env python3
"""Basic Redis caching module with call counting and call history"""

import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a method."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Store input args as string in Redis list
        self._redis.rpush(input_key, str(args))

        # Call original method
        result = method(self, *args, **kwargs)

        # Store output in Redis list
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
        Store data in Redis with a random UUID key.

        Args:
            data: Data to store (str, bytes, int, or float).

        Returns:
            The Redis key where data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Retrieve data from Redis by key and optionally convert it.

        Args:
            key: Redis key
            fn: Optional callable to convert the data

        Returns:
            The converted data or raw bytes if no fn provided.
            None if key does not exist.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

    def get_str(self, key: str) -> Optional[str]:
        """Automatically decode Redis bytes to UTF-8 string."""
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Automatically convert Redis bytes to integer."""
        return self.get(key, fn=lambda d: int(d))


def replay(method: Callable):
    """
    Display the history of calls of a particular function.

    Args:
        method (Callable): The method to replay.
    """
    redis_client = method.__self__._redis
    qualname = method.__qualname__

    count = redis_client.get(qualname)
    count = int(count) if count else 0

    print(f"{qualname} was called {count} times:")

    inputs_key = f"{qualname}:inputs"
    outputs_key = f"{qualname}:outputs"

    inputs = redis_client.lrange(inputs_key, 0, -1)
    outputs = redis_client.lrange(outputs_key, 0, -1)

    for inp, outp in zip(inputs, outputs):
        inp_str = inp.decode("utf-8")
        outp_str = outp.decode("utf-8")
        print(f"{qualname}(*{inp_str}) -> {outp_str}")
