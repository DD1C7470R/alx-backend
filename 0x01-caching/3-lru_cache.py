#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    RECENTLY_USED = []

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
                least_key = [
                    delkey for delkey in self.cache_data.keys()
                    if delkey not in self.RECENTLY_USED
                ]
                if len(least_key) > 0:
                    discarded_key = least_key[0]
                else:
                    discarded_key = self.RECENTLY_USED[0]
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.get_least_used(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        else:
            self.get_least_used(key)
            return self.cache_data.get(key)

    def get_least_used(self, key):
        """ Get least used item by key
        """
        if len(self.RECENTLY_USED) == BaseCaching.MAX_ITEMS:
            del self.RECENTLY_USED[0]
        self.RECENTLY_USED.append(key)
