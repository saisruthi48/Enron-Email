#!/usr/bin/python
import sys
result = {}
for line in sys.stdin:
    line = line.strip()
    id, count = line.split('\t',1)
    try:
        count = int(count)
        result[id] = result.get(id,0)+count
    except ValueError:
        pass
skeys = sorted(result.keys())
for key in skeys:
    print '%s\t%s' %(key,result[key])
