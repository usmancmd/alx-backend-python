#!/usr/bin/env python3
"""GithubOrgClient Test class"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from typing import Dict
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, test_org, mock_get_json):
        """test_org method"""
        expected_result = {'login': test_org}

        mock_get_json.return_value = expected_result

        test_instance = GithubOrgClient(test_org)

        result = test_instance.org

        mock_get_json
        .assert_called_once_with(
                f'https://api.github.com/orgs/{test_org}'
        )

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
