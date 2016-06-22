__author__ = "anubhav"


import urllib

url = "http://pythonprogramming.net"
values = {
    's' : 'basic',
    'submit' : 'search'
}

data = urllib.urlencode(values)
data = data.encode('utf-8')
req = urllib.urlopen(url,data)

respData = req.read()

print respData



