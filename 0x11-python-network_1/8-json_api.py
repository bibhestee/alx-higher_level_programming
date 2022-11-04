#!/usr/bin/python3
"""
    This python script takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""


def json_api():
    """
        json_api : get information from an api and return json data
        Requirement:
            - The input must be sent in the variable q
            - The output format should be [<id>] <name>
    """

    import sys
    import requests

    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) > 1:
        value = sys.argv[1]
    else:
        value = ""
    data = {'q': value}

    # Post a request to the api
    response = requests.post(url, data=data)
    try:
        content = response.json()
        if not content:
            print("No result")
        else:
            name = content.get('name')
            id = content.get('id')
            print(f"[{id}] {name}")
    except Exception:
        print("Not a valid JSON")


if __name__ == "__main__":
    json_api()
