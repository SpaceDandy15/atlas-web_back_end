#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that inherits from BaseCaching.
    It uses the First-In First-Out (FIFO) algorithm to discard items.
    """

    def __init__(self):
        """Initialize the FIFO cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache using FIFO algorithm.

        Args:
            key (str): The key under which the item is stored.
            item (Any): The item to be stored.

        If key or item is None, do nothing.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print("DISCARD:", first_key)

    def get(self, key):
        """
        Get an item by key.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
        Value associated with the key/None if not found or key is None.
        """
        return self.cache_data.get(key, None)
