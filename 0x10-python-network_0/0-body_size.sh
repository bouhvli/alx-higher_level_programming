#!/bin/bash
# takes, sends, and displays the size of the body of the response.
# taking the URL
URL_GIVEN=$1
# sends the request to the url
curl -w "%{size_download}\n" $URL_GIVEN