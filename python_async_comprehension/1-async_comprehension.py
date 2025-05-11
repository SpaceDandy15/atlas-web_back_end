#!/usr/bin/env python3
"""Coroutine that collects 10 numbers from an async generator"""

from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using async comprehension"""
    return [i async for i in async_generator()]
