#!/usr/bin/env python3
"""
Wait_random that waits for a random delay
between 0 and max_delay (included and float value) seconds
and eventually returns it
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay 4 between 0 and max_delay"""
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
