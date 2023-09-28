#!/bin/bash
# send a request to a URL passed as an argument, and displays only the status code of the response.
curl -s --head $1 | awk '/^HTTP/{print $2}' | tr -d '\n'
