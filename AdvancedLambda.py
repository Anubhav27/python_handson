__author__ = 'Anubhav'

import commands

nums = range(2,50)


print nums

sentence = "my name is anubhav nanda"

words =  sentence.split()

print words

lengths = map(lambda word : len(word), words)

print lengths

mount = commands.getoutput('mount -v')
lines = mount.splitlines()
points = map(lambda line: line.split(), lines)

print points
