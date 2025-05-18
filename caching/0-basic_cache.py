#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that inherits from BaseCaching.
    This cache has no limit on the number of items.
    """

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key (str): The key under which the item is stored.
            item (Any): The item to be stored.

        If key or item is None, do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
            The value associated with the key, or None if not found or key is None.
        """
        return self.cache_data.get(key, None)
