#!/usr/bin/python3
"""
    This python script fetch 'https://alx-intranet.hbtn.io/status'
"""


def hbtn_status():
    """ This functions fetches the url and return the data as a bytes file """
    from urllib import request

    req = request.Request('https://alx-intranet.hbtn.io/status')

    with request.urlopen(req) as response:
        return response.read()


if __name__ == '__main__':
    html = hbtn_status()
    print("Body response:")
    print(f"- type: {type(html)}")
    print(f"- content: {html}")
    print(f"- utf8 content: {html.decode('UTF-8')}")
