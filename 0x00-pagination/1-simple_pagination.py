#!/usr/bin/env python3
"""
Main file
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    desc: function to computes page indexes
    Args:
        page(int): page number
        page_size(int): size of page
    return:  a tuple of size two containing a start index
        and an end index corresponding to the range of
        indexes to return in a list for those particular
        pagination parameters
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        desc: method to return info of a page
        return: a list of data list or an empty list
        '''
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        first_idx, end_idx = index_range(page, page_size)

        try:
            return self.dataset()[first_idx: end_idx]
        except IndexError:
            return []
