import urllib
import re

symbolslist = ["APPL","FB","IBM"]

i=0
while i<len(symbolslist):
    url = "https://in.finance.yahoo.com/q?s=" +symbolslist[i] + "&ql=0"
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    print symbolslist[i].lower()
    regex = '<span id="yfs_l84_'+symbolslist[i].lower()+'">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern,htmltext)
    print "the price of",symbolslist[i], " is ",price[0]
    i+=1

#yahoourl = "https://in.finance.yahoo.com/q?"

