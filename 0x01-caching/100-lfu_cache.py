#!/usr/bin/env python3
'''
Module for implementing LFUCache class
'''
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''
    LFUCache implementation
    '''

    def __init__(self):
        super().__init__()
        # keep tack for least recently used
        self.access_ordered = []
        # keep tack for least frequently used
        self.access_count = {}

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

                self.access_count[key] += 1
            else:
                if len(self.cache_data) < super().MAX_ITEMS:
                    self.cache_data.update({key: item})
                    self.access_ordered.append(key)

                    self.access_count[key] = 1
                else:
                    access_count_values = list(self.access_count.values())

                    min_access_count = min(access_count_values)

                    keys_for_min_access_count = [
                        k for k, v in self.access_count.items()
                        if v == min_access_count
                    ]

                    if len(keys_for_min_access_count) == 1:
                        self.access_ordered.remove(
                            keys_for_min_access_count[0])
                        self.access_count.pop(keys_for_min_access_count[0])
                        self.cache_data.pop(keys_for_min_access_count[0])
                        print(f'DISCARD: {keys_for_min_access_count[0]}')
                    else:
                        # iterate to match the first item in
                        # self.access_ordered in keys_for_min_access_count
                        # this enables remove by LRU Algorithm
                        key_to_remove = ''
                        for key_item in self.access_ordered:
                            if key_item in keys_for_min_access_count:
                                key_to_remove = key_item
                                break

                        self.access_ordered.remove(key_to_remove)
                        del self.access_count[key_to_remove]
                        self.cache_data.pop(key_to_remove)
                        print(f'DISCARD: {key_to_remove}')

                    self.cache_data.update({key: item})
                    self.access_ordered.append(key)
                    self.access_count[key] = 1

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

            self.access_count[key] += 1

            return self.cache_data[key]

        return None
