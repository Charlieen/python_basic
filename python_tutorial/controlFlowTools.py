#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:53:47 2021

@author: dzgygmdhx
"""

a=['Mary','Charlie',"lena"]

for i in range(len(a)):
    print(a[i])

print(type(range(10)))

o= range(10)


print(sum(o))
print(list(o))

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break;
    else:
        print(n,'is a prime number')
        
for num in range(2,10):
    if num % 2 ==0:
        print("Found an event number",num)
        continue
    print("Found an odd number",num)
    
    
class MyEmptyClass:
    pass

def initLog(*args):
    pass # Remember to implement this;
    

def fib(n):
    """ Print a Fibonacci series up to n. """
    a,b = 0,1
    while a<n:
        print(a, end=" ")
        a,b = b,a+b
    print()
    
fib(100)

print(type(fib))
print(fib)

f1=fib

f1=None  # value reference

fib(100)

print(fib(0))

# Default Argument Values  some kind of same function name ,

# in keyword , test whether or not a sequence contains a certain value

def ask_ok(prompt,retries=4,reminder="Please try again"):
    while True:
        ok=input(prompt)
        if ok in ('y','ye','yes'):
            return True # return directlly quit the while loop
        elif ok in ('n','no','nop','nope'):
            return False
        retries = retries-1
        if retries <0:
            raise ValueError('invalid user response')
        print(reminder)

# ask_ok("Do you really want to quity?")
# ask_ok("Do you really want to quity?",2,"go ahead,come on")
# ask_ok("Do you really want to quity?",5,"you can try another once")


# the default values are evaluated at the point of function definition in the defining scope,

i=5

def f(arg=i):
    print(arg)

i=6
f()

### when the functinon was called, the default value is evaluated only once, eventhough, the same
# function was called many times; but be carefully this mutable variable:
    

def f(a,L=[]):
    L.append(a)
    return L


print(f(1))

print(f(2))
print(f(3))


def f(a,L=None):
    if L is None:
        L=[]
        L.append(a)
        return L
    
print(f(1))

print(f(2))
print(f(3))













