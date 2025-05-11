#!/usr/bin/env python3
"""Return asyncio.Task of wait_random."""
import asyncio
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return Task that runs wait_random with max_delay."""
    return asyncio.create_task(wait_random(max_delay))
