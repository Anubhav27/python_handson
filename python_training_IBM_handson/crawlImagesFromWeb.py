import urllib2
import re
import sys

raw_url_input = raw_input("enter a url to extract image from\n")

print raw_url_input

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

req = urllib2.Request(raw_url_input, headers=hdr)

open_url = urllib2.urlopen(req)

url_text = open_url.read()

fopen_write = open('lush_html.txt','w')

sys.stdout = fopen_write;

print url_text

sys.stdout.close()

fopen_write.close()



