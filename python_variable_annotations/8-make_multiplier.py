#!/usr/bin/env python3
"""
Returns a function that multiplies a float by a given multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies its float input by `multiplier`.

    Args:
        multiplier (float): The value to multiply by.

    Returns:
        Callable[[float], float]: Function multiplies its input by multiplier.
    """
    return lambda x: x * multiplier
