#!/usr/bin/python3
"""
    This python script takes GitHub credentials (username and password) and
        uses the GitHub API to display id
"""


def my_github():
    """ Get github credentials using the GitHub API to display id """

    import sys
    import requests

    usr = sys.argv[1]
    pwd = sys.argv[2]
    url = f"https://api.github.com/users/{usr}"

    response = requests.get(url, auth=(usr, pwd))
    data = response.json()
    id = data.get('id')
    print(id)


if __name__ == "__main__":
    my_github()
