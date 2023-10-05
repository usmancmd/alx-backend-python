"""
Given the parameters and the return values,
add type annotations to the function
"""

from typing import Mapping, Union, Any, TypeVar


def safely_get_value(dct: Mapping, key:Any, default: Union[TypeVar('T'), None] = None)\
        -> Union[Any, TypeVar('T')]:
    if key in dct:
        return dct[key]
    else:
        return default
