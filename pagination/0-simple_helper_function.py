#!/usr/bin/env python3
"""
Simple helper function for pagination.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Return a tuple containing the start and end index for a page of data.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: The start index (inclusive) and end index (exclusive).
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
