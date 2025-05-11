#!/usr/bin/env python3
"""
Returns a tuple with a string and square of a number.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple: (k, v squared as float)

    Args:
        k (str): A string.
        v (int | float): A numeric value.

    Returns:
        Tuple[str, float]: The string and the square of the value.
    """
    return (k, float(v ** 2))
