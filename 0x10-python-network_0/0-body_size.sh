#!/usr/bin/bash
# This bash script takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI ${1} | grep -oP 'Content-Length: \K\d+' -
