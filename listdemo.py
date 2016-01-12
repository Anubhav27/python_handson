__author__ = 'Anubhav'


shoplist = ['a','b','c','d']

print shoplist.__len__()


shoplist.append('e')

print shoplist.__len__()

shoplist.append('z')

shoplist.append('f')


print shoplist.__len__()


print shoplist


shoplist.sort()

print shoplist


for items in shoplist:
    print items

for i in range(100):
    print i

