#!/usr/bin/env python3
"""Run task_wait_random concurrently."""
import asyncio
from typing import List
from tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Call task_wait_random n times and return delays sorted."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
