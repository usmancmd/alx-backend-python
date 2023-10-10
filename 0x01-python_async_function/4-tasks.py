#!/usr/bin/env python3
"""
Code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called
"""
import asyncio
from typing import List
from heapq import heappush, heappop

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times"""
    heap = []
    delays = []

    for _ in range(n):
        delay = await task_wait_random(max_delay)
        heappush(heap, delay)

    while heap:
        delays.append(heappop(heap))

    return delays
