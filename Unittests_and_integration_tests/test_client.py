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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the list of repo names from mocked payload."""
        test_repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = test_repos_payload

        client = GithubOrgClient("some_org")

        with patch.object(GithubOrgClient, "_public_repos_url", new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = "http://fakeurl.com/repos"
            repos = client.public_repos()

            # Check that the repo names list is correct
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])

            # Assert the mocks were called once
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("http://fakeurl.com/repos")


if __name__ == "__main__":
    unittest.main()
