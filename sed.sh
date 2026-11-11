#!/bin/bash
HANIMCODE=.
cat ./centers.txt
# cat ./WScenters.txt
# /usr/bin/grep 'class="Code"' ./standards/{A.2,A.4,A.6,A.8,A.10}.txt | sed -e 's/.*class="Code">//' -e 's/<.*//'
# cat found*centers*.txt

/usr/bin/grep 'class="Code"' $HANIMCODE/standards/A.10.txt | sed -e 's/.*class="Code">//' -e 's/<.*//'
