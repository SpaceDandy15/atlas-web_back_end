#!/usr/bin/env python3
""" MRUCache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that discards
    the Most Recently Used items first.
    """

    def __init__(self):
        """Initialize the MRU cache"""
        super().__init__()
        self.usage_order = []  # Track usage order

    def put(self, key, item):
        """
        Add an item to the cache using MRU replacement policy.

        Args:
            key (str): Key to store in cache
            item (any): Value associated with the key

        If either key or item is None, do nothing.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the most recently used item
            mru_key = self.usage_order.pop()
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        # Add new item and mark as most recently used
        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """
        Retrieve an item by key and update its usage.

        Args:
            key (str): The key to look up

        Returns:
            The cached value, or None if key doesn't exist or is None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
