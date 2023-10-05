#!/usr/bin/env python3
"""
Type-annotated function to_kv that
takes a string k and an int OR float v as
arguments and returns a tuple
"""

from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[Union[str, float]]:
    """Returns a tuple"""
    return (k, v ** 2)
