#!/usr/bin/env python3
"""
Function to sum a list of ints and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a mixed list of ints and floats.

    Args:
        mxd_lst (List[Union[int, float]]): List containing ints and floats.

    Returns:
        float: Total sum.
    """
    return sum(mxd_lst)
