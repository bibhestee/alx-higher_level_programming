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
    import requests
    import sys

    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    response = requests.post(url, data=value)
    print(response.text)


if __name__ == "__main__":
    post_email()
