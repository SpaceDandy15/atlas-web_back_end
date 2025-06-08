#!/usr/bin/env python3
"""Basic Redis caching module with call counting"""

import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        new_count = self._redis.incr(key)
        print(f"[DEBUG] Incremented {key}: {new_count}")
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value


if __name__ == "__main__":
    cache = Cache()
    print("Qualname:", cache.store.__qualname__)

    cache.store(b"first")
    count = cache.get(cache.store.__qualname__)
    print(f"Count after 1 store: {count} (int: {int(count)})")

    cache.store(b"second")
    cache.store(b"third")
    count = cache.get(cache.store.__qualname__)
    print(f"Count after 3 stores: {count} (int: {int(count)})")
