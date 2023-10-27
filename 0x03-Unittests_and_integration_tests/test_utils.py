#!/usr/bin/env python3
"""Test utils module"""

import unittest
from parameterized import parameterized
import utils


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map, path, expected_result):
        """test_access_nested_map method"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected_result)


if __name__ == "__main__":
    unittest.main()
