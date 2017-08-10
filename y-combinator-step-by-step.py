#!/usr/bin/env python

fib = lambda x: 1 if x < 2 else fib(x-1) + fib(x-2)

#
# A simple factorial function like:
factorial = lambda x: 1 if x < 2 else x * factorial(x-1)
print "Original:"
print " * factorial() 5!", [ factorial(x) for x in range(1, 5) ]

#
# The goal is to parameterize factorial function
# reference: https://stackoverflow.com/questions/93526/what-is-a-y-combinator

#
# step 1: Parameterize factial function
#         We first create an other function call
#         recursive, and call the origial factorial.
#

def factorial(recursive):
    return lambda x: 1 if x < 2 else x * recursive(x-1)

def recursive(n):
    return factorial(recursive)(n)

print "Step 1: parameterize factorial"
print " * recursive() 5!", [ recursive(x) for x in range(1, 5) ]

#
# step 2: In step 1 we successfully create a recursive
#         function to parameterize factorial(). This time
#         we focus on parameterize recursive().
def recursive(f):
    return factorial(lambda x: f(f)(x))

print "Step 2: parameterize recursive"
print " * recursive(recursive)() 5!", [ recursive(recursive)(x) for x in range(1, 5) ]

#
# step 3: Now, instead of calling recursive(recursive),
#         we create a wrapper called Y()
def Y():
    return (lambda f: f(f))(recursive)

print "Step 3: A Y wrapper"
print " * Y() 5!", [ Y()(x) for x in range(1, 5) ]

#
# step 4: Now we replace recursive parameter with its
#         definition (i.e. lambda f: factorial(lambda x: f(f)(x)))
#
def Y():
    return (lambda f: f(f))(lambda f: factorial(lambda x: f(f)(x)))

print "Step 3: Convert and expand recursive in Y()"
print " * Y() 5!", [ Y()(x) for x in range(1, 5) ]

#
# step 5: At the final, we want to parameterize factorial, simplily
#         pass it as parameter f.
#
# Finally we get a generic solution, Y combinator
def Y(f):
    return (lambda g: g(g))(lambda g: f(lambda x: g(g)(x)))
Y = lambda f: (lambda g: g(g))(lambda g: f(lambda x: g(g)(x)))

print "Step 4: parameterize factorial in Y()"
print " * Y(lambda factor: lambda x: 1 if x < 2 else x * factor(x-1))", \
       [ Y(lambda factor: lambda x: 1 if x < 2 else x * factor(x-1))(x) for x in range(1, 5) ]
