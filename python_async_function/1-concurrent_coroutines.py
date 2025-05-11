#!/usr/bin/env python3
"""
Defines `wait_n` coroutine to spawn `wait_random` n times and return delays
in ascending order.
"""

import asyncio
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Calls `wait_random` n times and returns delays in ascending order.

    Parameters:
    n (int): Number of `wait_random` calls.
    max_delay (int): Maximum delay for each call.

    Returns:
    List[float]: Sorted list of delays.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*delays))
