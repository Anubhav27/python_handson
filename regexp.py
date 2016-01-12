__author__ = 'Anubhav'


#program to search for email in a string
import re
str = 'my email id is anubhav.nanda@gmail.com and pallavianubhav@gmail.com'

#match = re.search(r'[\w.-]+@[\w.-]+', str)
emails = re.findall(r'[\w.-]+@[\w.-]+', str)

for m in emails:
    print m
    #print match.group(1)
    #print match.group(2)