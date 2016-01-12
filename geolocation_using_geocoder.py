__author__ = 'Anubhav'


import urllib

response = urllib.urlopen('http://api.hostip.info/get_html.php?ip=10.0.0.9&position=true').read()

print(response)



