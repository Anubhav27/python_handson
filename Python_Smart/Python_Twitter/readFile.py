__author__ = 'Anubhav'

#import ConfigParser


#config =  ConfigParser.RawConfigParser()

#config.read("scale.properties")

#print config.get('Cluster','node')



props={}


def readFile():
    with open("scale.properties","r") as f:
        for line in f:
            l = line.strip()
            value = l.split("=")
            #print value
            props[value[0].strip()] = value[1].strip()
    return props


props = readFile()

print props['node']







