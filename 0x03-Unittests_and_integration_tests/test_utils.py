#!/usr/bin/env python3
"""Test utils module"""

import unittest
from unittest.mock import patch
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
        self.assertEqual(utils.access_nested_map(nested_map, path),
                         expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test_access_nested_map_exception method"""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""
    def test_get_json(self):
        """test_get_json method"""
        test_url_payload = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]

        for test_url, test_payload in test_url_payload:
            with patch('utils.requests.get') as mocked_get:
                mock_response = mocked_get.return_value
                mock_response.json.return_value = test_payload

                result = utils.get_json(test_url)

                mocked_get.assert_called_with(test_url)
                self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
