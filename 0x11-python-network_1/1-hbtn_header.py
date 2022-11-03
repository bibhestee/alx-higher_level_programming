#!/usr/bin/python3
"""
    This Python script takes in a URL, sends a request to the URL
        and displays the value of the X-Request-Id variable
        found in the header of the response
"""


def hbtn_header():
    """
        Returns the header response from http get request
    """
    import sys
    from urllib import request
    req = request.Request(sys.argv[1])
    with request.urlopen(req) as response:
        return response.headers


if __name__ == "__main__":
    header = hbtn_header()
    id = header.get("X-Request-Id")
    print(id)
