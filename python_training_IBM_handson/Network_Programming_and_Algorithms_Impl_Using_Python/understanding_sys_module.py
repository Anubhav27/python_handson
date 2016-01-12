import sys

#this will print system version
print sys.version

#this will print arguements passed to script
print sys.argv

#this will print number of arguements passed to script
print len(sys.argv)


#iterating through list of arguemnts passed to python

"""for i in range(len(sys.argv)):
    if i==0:
        print "Function name: %s" % sys.argv[0]
    else:
        print "%d. arguement: %s" % (i,sys.argv[i])
"""

"""for i in (sys.stdin,sys.stdout,sys.stderr):
    print(i)"""

save_stderr = sys.stderr
fh = open("errors.txt","w")

sys.stderr = fh

x = 10 / 0

sys.stderr = save_stderr

fh.close()
