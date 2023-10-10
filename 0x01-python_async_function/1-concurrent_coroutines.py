#!/usr/bin/env python3
"""
Async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay
"""
import asyncio
from typing import List
from heapq import heappush, heappop

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times"""
    heap = []
    delays = []

    for _ in range(n):
        delay = await wait_random(max_delay)
        heappush(heap, delay)

    while heap:
        delays.append(heappop(heap))

    return delays
