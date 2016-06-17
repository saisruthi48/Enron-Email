#!/usr/bin/python
import sys
for line in sys.stdin:
    for word in line.strip().split():
        print("{0}\t{1}".format(word, 1))
