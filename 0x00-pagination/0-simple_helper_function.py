#!/usr/bin/env python3
"""
Main file
"""


def index_range(page: int = None, page_size: int = None) -> tuple:
    start = (page * page_size) - page_size
    end = page * page_size
    return (start, page * page_size)
