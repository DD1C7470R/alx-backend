#!/usr/bin/env python3
"""
Main file
"""


def index_range(page: int = None, page_size: int = None) -> tuple:
    """Retrieves the index range from a given page and page size.
    """
    if page and page_size:
        if page > 1:
            start = (page * page_size) - page_size
            return (start, page * page_size)
        else:
            return (0, page_size)
    else:
        return (0, 0)
