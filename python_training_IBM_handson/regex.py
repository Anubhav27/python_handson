import re

str = "my email id is anubhav.nanda@gmail.com"

#using match to search pattern in a string
match = re.search(r'([\w.-]+)@([\w.-]+)',str)

if match:
    print 'found :',match.group()
    print 'found : ',match.group(1)
    print 'found : ',match.group(2)
else:
    print "no match found"

