#!/bin/bash
curl -sI ${1} -o "file.txt"
grep -Po 'HTTP\S1.1\s\K\d+' file.txt
