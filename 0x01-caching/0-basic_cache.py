#!/usr/bin/env python3
'''
Module for implementing BasicCache class
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    BasicCache implementation
    This caching system doesn’t have limit
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
