#!/usr/bin/env python3
"""
Main file
"""


def index_range(page: int = None, page_size: int = None) -> tuple:
    start = (page - 1) * page_size
    return (start, page * page_size)
