#!/usr/bin/env python3
"""
Function to sum a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of a list of floats.

    Args:
        input_list (List[float]): List of floats.

    Returns:
        float: Total sum.
    """
    return sum(input_list)
