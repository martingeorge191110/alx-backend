#!/usr/bin/env python3
"""module containing MRUCache class"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class that uses MRU caching system"""

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(list(self.cache_data.keys())) == self.MAX_ITEMS:
                    most_recently_used_key = self.cache_data.popitem()
                    print(f"DISCARD: {most_recently_used_key[0]}")
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return (value)
        else:
            return (None)
