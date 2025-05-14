#!/usr/bin/env python3
"""module containing BasicCache class"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache Class"""

    def put(self, key, item):
        """puts a cache item in cache_data attribute"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """gets a cache item from cache_data by key"""
        if key is not None and key in list(self.cache_data.keys()):
            return (self.cache_data[key])

        return (None)
