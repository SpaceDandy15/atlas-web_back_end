#!/usr/bin/env python3
"""Unittests for GithubOrgClient"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct payload"""
        # Define what mock_get_json should return
        mock_get_json.return_value = {"login": org_name}

        # Instantiate client and call .org
        client = GithubOrgClient(org_name)
        result = client.org

        # Assert the result matches the mocked payload
        self.assertEqual(result, {"login": org_name})

        # Assert get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test that _public_repos_url property returns the correct URL based on the mocked org payload."""
        test_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}

        client = GithubOrgClient("google")

        # Patch the 'org' property of the client instance to return test_payload
        with patch.object(GithubOrgClient, "org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = test_payload
            result = client._public_repos_url
            self.assertEqual(result, test_payload["repos_url"])


if __name__ == "__main__":
    unittest.main()
