#!/usr/bin/env bash

# Get the URL from the command line argument
url="$1"

# Send a request to the URL using curl and save the output to a variable
response=$(curl -sI $url)

# Extract the Content-Length header from the response
content_length=$(echo "$response" | grep -i "Content-Length:" | awk '{print $2}' | tr -d '\r')

# Print the size of the body in bytes
echo $content_length

