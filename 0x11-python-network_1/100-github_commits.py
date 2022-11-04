#!/usr/bin/python3
"""
This Python script that takes 2 arguments in order to solve this challenge.

Requirement:
    The first argument will be the repository name
    The second argument will be the owner name
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    You don’t need to check arguments passed to the script (number or type
"""


def github_commit():
    """ List 10 commits (from the most recent to oldest) """
    import sys
    import requests

    usr = sys.argv[1]
    repo = sys.argv[2]

    url = f"https://api.github.com/repos/{usr}/{repo}/commits"
    response = requests.get(url)
    commits = response.json()

    print(commits)
#    count = 0
#    for item in commits:
#        if count == 10:
#            return
#        sha = item.get('sha')
#        author = item.get('commit').get('author').get('name')
#        print(f'{sha}: {author}')
#        count += 1


if __name__ == "__main__":
    github_commit()
