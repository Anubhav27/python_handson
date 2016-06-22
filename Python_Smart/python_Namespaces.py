__author__ = 'Anubhav'



#dir() : all variables,functions,classess,constants declared in the module
#globals() : lists all global namespaces
#locals() : lists all local namespaces


def sum(a,b):
    c = a+b
    return c


def main():
    print "First module name : {}".format(__name__)
    s = sum(2,3)
    print s


if __name__ == '__main__':
    main()




