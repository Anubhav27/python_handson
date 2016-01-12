__author__ = 'Anubhav'

def say(message, times=1):
    print message * times

say('a')
say('a', 5)


def total(initial=5, *numbers, **keywords):
    count = initial

    for number in numbers:
        count += number
    for key in keywords :
        count += keywords[key]


    return count

print total(10, 1, 2, 3, vegetables=50, fruits=100)


print max(2,3)

#to print documentation string
def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

print_max(3, 5)
print print_max.__doc__