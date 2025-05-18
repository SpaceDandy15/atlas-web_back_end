#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that inherits from BaseCaching.
    It uses the Last-In First-Out (LIFO) algorithm to discard items.
    """

    def __init__(self):
        """Initialize the LIFO cache"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add an item in the cache using LIFO algorithm.

        Args:
            key (str): The key under which the item is stored.
            item (Any): The item to be stored.

        If key or item is None, do nothing.
        """
        if key is None or item is None:
            return

        if key in self.stack:
            self.stack.remove(key)
        self.stack.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop(-2)
            del self.cache_data[last_key]
            print("DISCARD:", last_key)

    def get(self, key):
        """
        Get an item by key.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
            The value associated with the key/None if not found or key is None.
        """
        return self.cache_data.get(key, None)
