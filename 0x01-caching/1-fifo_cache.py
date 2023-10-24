#!/usr/bin/env python3
'''
Module for implementing FIFOCache class
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    FIFOCache implemntation
    '''

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''
        desc: adds item to the cache_data dict
        Args:
            key: dict key
            item: dict item
        return: None
        '''
        if key and item:
            if len(self.cache_data) < super().MAX_ITEMS:
                self.cache_data.update({key: item})
            else:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.cache_data.update({key: item})
                else:
                    key_to_discard = list(self.cache_data.keys())[0]
                    self.cache_data.pop(key_to_discard)
                    print(f'DISCARD: {key_to_discard}')
                    self.cache_data.update({key: item})

    def get(self, key):
        '''
        desc: retrives an item from the cache data
        Args:
            key: dict key
        return: If key is None or if the key doesn't
            exist in self.cache_data, return None.
        '''

        return self.cache_data.get(key) if key else None
