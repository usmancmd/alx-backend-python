#!/usr/bin/env python3
"""
Measure_time function with integers n and max_delay
as arguments that measures the total execution time
for wait_n(n, max_delay), and returns total_time / n
"""
from time import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns total time of execution divided by n"""
    start_time = time() # time() gives current time in secs
    asyncio.run(wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time
    return total_time / n

