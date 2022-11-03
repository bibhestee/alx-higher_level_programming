#!/usr/bin/python3
"""
    This script takes  in a URL, sends a request to the URL
        and displays the body of the response
"""


def error_code():
    """ Prints the HTTP status code greater than or equal to 400 """
    import requests
    import sys

    a_url = sys.argv[1]
    response = requests.get(a_url)
    status = response.status_code
    content = response.content.decode('UTF-8')
    if status >= 400:
        print(f"Error code: {status}")
    else:
        print(content)


if __name__ == "__main__":
    error_code()
