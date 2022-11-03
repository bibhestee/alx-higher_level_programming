#!/usr/bin/python3
"""
    This python script takes in a URL and an email, sends a POST request to the
        passed URL with the email as a parameter, and displays the body of the
        response(decoded in utf-8)
"""


def post_email():
    """
        Requirement:
            email: email variable to be POST
    """
    from urllib import request, parse
    import sys

    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    data = parse.urlencode(value).encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        html = response.read().decode('UTF-8')
        print(html)


if __name__ == "__main__":
    post_email()
