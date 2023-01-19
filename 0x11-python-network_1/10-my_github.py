#!/usr/bin/python3
"""
    This python script takes GitHub credentials (username and password) and
        uses the GitHub API to display id
"""


def my_github():
    """ Get github credentials using the GitHub API to display id """

    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get('https://api.github.com/user', auth=basic)
    print(response.json().get('id'))


if __name__ == "__main__":
    my_github()
