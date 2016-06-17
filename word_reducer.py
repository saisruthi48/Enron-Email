#!/usr/bin/python

#from operator import itemgetter
import sys

result = {};
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
        result[word] = result.get(word, 0) + count
    except ValueError:
        pass
skeys = sorted(result.keys())
for key in skeys:       
    print '%s\t%s' %(key,result[key])


