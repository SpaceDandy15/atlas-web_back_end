#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache is a caching system that discards the least recently used items first.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """Initialize the LRU cache"""
        super().__init__()
        self.order = []  # Keeps track of access order

    def put(self, key, item):
        """
        Add an item to the cache using LRU replacement policy.

        Args:
            key (str): Key to store in cache
            item (any): Value associated with the key

        If either key or item is None, do nothing.
        """
        if key is None or item is None:
            return

        # If key exists, update and refresh usage
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove least recently used item
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        # Add the new item and update usage order
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Retrieve an item by key and update its usage as most recent.

        Args:
            key (str): The key to look up

        Returns:
            The cached value, or None if key doesn't exist or is None.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update key's position as most recently used
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
