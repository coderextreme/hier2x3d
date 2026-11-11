#!/bin/bash
/usr/bin/grep 'class="Code"' ./standards/A.3.txt ./standards/A.5.txt ./standards/A.7.txt ./standards/A.9.txt ./standards/A.11.txt | sed -e 's/.*class="Code">//' -e 's/<.*//'
# cat found*translations*.txt

# /usr/bin/grep 'class="Code"' A.11.txt | sed -e 's/.*class="Code">//' -e 's/<.*//'
