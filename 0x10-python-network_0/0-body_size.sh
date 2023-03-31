#!/bin/bash
# Displays the size of the body of the response
curl -s -o /dev/null  -w "%{http_code}" "$1" ; echo ""
