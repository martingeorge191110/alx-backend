#!/usr/bin/env python3
"""module containing FIFOCache Class"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache Class uses FIFO Caching"""

    def put(self, key, item):
        """ Add item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(list(self.cache_data.keys())) > self.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """ Get item by key"""
        return (self.cache_data.get(key, None))
