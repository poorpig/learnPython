#!/usr/bin/env python

#'test.py -- create text file

import os
ls = os.linesep

print "entry your file name:\n"

fname = raw_input()

#get file
if os.path.exists(fname):
    print "ERROR: '%s' has exists" % fname


#get file content (text) lines
all = []
print "\nEnter lines ('.' by itself to quit). \n"

#loop until user terminates input
while True: 
	entry = raw_input('> ')
	if entry == '.':
		break
	else:
		all.append(entry)

#write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print 'done!'