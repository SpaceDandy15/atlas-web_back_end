#!/usr/bin/env python3
"""
Annotate function to return list of tuples with item and its length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements and their lengths.

    Args:
        Iterable of sequence items (like str, list, tuple).

    Returns:
        List[Tuple[Sequence, int]]: Tuples with each element and its length.
    """
    return [(i, len(i)) for i in lst]
