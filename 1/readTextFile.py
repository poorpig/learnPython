#!/usr/bin/env python

'readTextFile.py -- read and idsplay text file'

# get filename
fname = raw_input('Enter filename:')
print 
# attempt to open file for reading

try:
    fobj = open(fname, 'r')
except IOError, e:
    print "*** file open error:", e
else:
    for eacheLine in fobj:
        print eacheLine
    fobj.close()
finally:
    print "DONE!"