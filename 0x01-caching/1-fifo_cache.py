#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
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
            if (
                size_of_cache > BaseCaching.MAX_ITEMS
                and key not in self.cache_data.keys()
            ):
                first_key, first_value = (
                    next(iter(self.cache_data.items()), (None, None))
                )
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        else:
            return self.cache_data.get(key)
