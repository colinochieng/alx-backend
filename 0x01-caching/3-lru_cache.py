#!/usr/bin/env python3
'''
Module for implementing LRUCache class
'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''
    LRUCache implementation
    '''

    def __init__(self):
        super().__init__()
        self.access_ordered = []

    def put(self, key, item):
        '''
        desc: adds item to the cache_data dict
        Args:
            key: dict key
            item: dict item
        return: None
        '''
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.access_ordered.remove(key)
                self.access_ordered.append(key)
            else:
                if len(self.cache_data) < super().MAX_ITEMS:
                    self.cache_data.update({key: item})
                    self.access_ordered.append(key)
                else:
                    lru_key = self.access_ordered.pop(0)
                    self.cache_data.pop(lru_key)
                    print(f'DISCARD: {lru_key}')
                    self.cache_data.update({key: item})
                    self.access_ordered.append(key)

    def get(self, key):
        '''
        desc: retrives an item from the cache data
        Args:
            key: dict key
        return: If key is None or if the key doesn't
            exist in self.cache_data, return None.
        '''
        if key in self.cache_data:
            self.access_ordered.remove(key)
            self.access_ordered.append(key)

        return self.cache_data.get(key) if key else None
