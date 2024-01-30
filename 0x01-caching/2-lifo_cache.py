#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        else:
            size_of_cache = len(self.cache_data.values()) + 1
            if key in self.cache_data.keys():
                del self.cache_data[key]
            elif size_of_cache > BaseCaching.MAX_ITEMS:
                discarded_key, discarded_value = self.cache_data.popitem()
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        else:
            return self.cache_data.get(key)
