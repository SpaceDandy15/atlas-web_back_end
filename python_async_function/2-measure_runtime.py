#!/usr/bin/env python3
"""Measure runtime of wait_n using asyncio."""
import time
from typing import Callable
from concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure average execution time of wait_n.

    Args:
        n: number of times to run wait_random
        max_delay: max wait time

    Returns:
        Average time per coroutine.
    """
    start = time.perf_counter()
    # Run the async function
    __import__('asyncio').run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
