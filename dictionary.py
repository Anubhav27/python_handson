__author__ = 'Anubhav'

dict = {}
dict['a'] = 'apple'
dict['b'] = 'ball'
dict['c'] = 'cat'

# print dictionary
print dict

#print first element in dictionary with key a
print dict['a']

#updating dictionary value forparticular key
dict['a'] = 6


print dict

#default iterating over dictionary iterate over its keys
#print keys in dictionary
for keys in dict.keys():
    print keys

#print keys in sorted order

for keys_sorted in sorted(dict.keys()):
    print keys_sorted, dict[keys_sorted]

print dict.items()
for k,v in dict.items():
    print k, '>' , v

#dictionary formatting using % to read string by name from dictionary

hash = {}
hash['word'] = 'garfield'
hash['count'] = 42

s = 'I want %(count)d copies of %(word)s' % hash

print s


