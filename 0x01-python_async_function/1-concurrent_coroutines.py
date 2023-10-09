#!/usr/bin/env python3
"""
Async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay
"""

import asyncio
import operator

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """wait_n spawn wait_random n times with the specified max_delay"""
    delays = []
    for _ in range(n):
        delay_time = await wait_random(max_delay)
        await asyncio.sleep(delay_time)
        delays.append((delay_time,))
        delays = sorted(delays, key=operator.itemgetter(0))
    delays = [delay[0] for delay in delays]
    return delays
