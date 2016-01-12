__author__ = 'Anubhav'

import sys

print sys.path[0]

print('The command line arguments are:')
for i in sys.argv:
    print i

print '\n\nThe PYTHONPATH is', sys.path, '\n'


