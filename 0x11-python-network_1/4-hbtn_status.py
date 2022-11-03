#!/usr/bin/python3
"""
    This python script fetch 'https://alx-intranet.hbtn.io/status'
"""


def hbtn_status():
    """ This functions fetches the url and return the data as a bytes file """
    import requests

    response = requests.get('https://alx-intranet.hbtn.io/status')
    content = response.content.decode('UTF-8')
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")


if __name__ == '__main__':
    hbtn_status()
