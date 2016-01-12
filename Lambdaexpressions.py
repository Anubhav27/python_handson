__author__ = 'Anubhav'

#Normal way of executing the expressions without lambda expressions
def f(x) : return x ** 2


print f(8)


# To use lambda expressions
g = lambda x : x ** 2

print g(4)




def make_increment(n) : return lambda x : x + n

f = make_increment(2)

g = make_increment(4)

print f(42),g(42)

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

print filter(lambda x: x % 3 == 0, foo)

