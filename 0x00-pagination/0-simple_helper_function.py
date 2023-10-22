#!/usr/bin/env python3
'''
Module for defining an auxilary function that
computes the index of index required
Page numbers are 1-indexed, i.e. the first page is page 1.
'''
from typing import Tuple


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
