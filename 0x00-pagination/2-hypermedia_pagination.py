#!/usr/bin/env python3
"""
Main file
"""

import csv
import math
from typing import List


index_range = __import__('0-simple_helper_function').index_range


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
        """get page to paginate a database of popular baby names.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        i_range = index_range(page, page_size)
        return [
            self.dataset()[idx] for idx in range(i_range[0], i_range[1])
            if idx <= len(self.dataset())
        ]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """get page to paginate a database of popular baby names.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        i_range = index_range(page, page_size)
        data_size = len(self.dataset())
        data = [
            self.dataset()[idx]
            for idx in range(i_range[0], i_range[1])
            if idx <= data_size
        ]
        total_pages = math.ceil(data_size / page_size)
        next_page = page + 1 if page + 1 < total_pages else None
        prev_page = page - 1 if page - 1 > 0 else None
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
