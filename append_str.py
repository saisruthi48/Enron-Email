#!/usr/bin/python
import glob
list = glob.glob("/Users/apple/Desktop/sample/sent/*")
print(list)
for f in list:
    file = open(f ,"a");
    file.write("######EA#####");
    file.close()

