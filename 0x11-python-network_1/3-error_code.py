#!/usr/bin/python3
"""
    This script takes  in a URL, sends a request to the URL
        and displays the body of the response
"""


def error_code():
    """
        Requirements:
            - manage urllib.error.HTTPError exceptions
    """
    from urllib import request, error
    import sys

    a_url = sys.argv[1]
    req = request.Request(a_url)
    try:
        with request.urlopen(req) as response:
            html = response.read().decode('UTF-8')
            print(html)
    except error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    error_code()
