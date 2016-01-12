__author__ = 'Anubhav'


for i in range(1,5):
    print i


while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        continue
    if len(s) > 5:
        break
print 'Done'