#!/usr/bin/python3
"""
    This python script fetch 'https://alx-intranet.hbtn.io/status'
"""


def hbtn_status():
    """ This functions fetches the url and return the data as bytes file """
    from urllib import request

    req = request.Request('https://alx-intranet.hbtn.io/status')

    with request.urlopen(req) as response:
        return response.read()


if __name__ == '__main__':
    html = hbtn_status()
    print(f"""Body response:
    - type: {type(html)}
    - content: {html}
    - utf8 content: {html.decode('UTF-8')}""")
