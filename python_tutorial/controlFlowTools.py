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

### Keyword Arguments

def parrot(voltage, state='a stiff' , action='voom',type="Norwegian Blue"):
    print("---This parrot wouldn't",action,end=" ")
    print("if you put",voltage,"volts through it.")
    print("Lovely plumage,the", type)
    print("-- It's",state,"!")
    
parrot(1000)
parrot(voltage=1090)
parrot(voltage=10292, action="break")
parrot('a million','bereft of life','jump') # 3 positional arguments
parrot('a thousound',action="just ok") #1 positional , 1 keyword


# all the following calls would be invalid

# parrot() # required argument missing
# parrot(voltage=5.0,'dead') # non-keyword argument after a keyword argument
# parrot(110,voltage=390) # duplicate value for the same argument
# parrot(actor="lilianjie")# unknown keyword argument

# No argument may receive a value more than once

def function(a):
    pass

# TypeError: function() got multiple values for argument 'a'
# function(0,a=1010)

## kind    is formal parameter
#  **name  receives a dictionary
#  *name   receives a tuple (containing the positional arguments beyond the formal parameter)
#  *name   must occur before **name
## 
def cheeseshop(kind,*arguments,**keywords):
    print("-- Do you have any",kind,"?")
    print("-- I'm sorry, we're all out of",kind)
    for arg in arguments:
        print(arg)
    print("-"*40)
    for kw in keywords:
        print(kw,":",keywords[kw])
        
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           # shopkeeper="Michael Palin", # SyntaxError: positional argument follows keyword argument
           ('d','ed'),
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")      


# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only


def standard_arg(arg):
    print(arg)

def pos_only_arg(arg1,arg2,/):
    print(arg1,arg2)
    
def kwd_only_arg(*,arg):
    print(arg)

def combined_example(pos_only,/,standard,*,kw_only):
    print(pos_only,standard,kw_only)
    

standard_arg(2)
standard_arg(arg=20)

pos_only_arg(3, 33)
# pos_only_arg(3, arg=33) # TypeError: pos_only_arg() got an unexpected keyword argument 'arg'

kwd_only_arg(arg=12)
# kwd_only_arg(12) #TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

combined_example(1, standard=90, kw_only=989)
combined_example(1, 90, kw_only=989)


### has a potential collision between the positional argument name and **kwds which has name as a key
# 1: name is positional parameter
# 2:  in **kwds  recieve a dictionary, in dic key should not eqaual name otherwise  
#     TypeError: foo() got multiple values for argument 'name'
# argument can have many type ,but fianl they are all argument, can not duplicated without ambiguity

def foo(name,**kwds):
    return 'ket' in kwds

print( foo(1,**{'name3':2,'ket':9090}))


## Arbitrary Argument Lists

def write_multiple_items(file,separator,*args):
    file.write(separator.join(args))
    
def concat(*args,sep="/"):
    return sep.join(args)

print( concat("earth","mars","venus"))

## Unpacking Argument Lists 
# * operator can unpack the arguments out of a list or tuple
# ** operator can unpack the arguments out of a dictionary

print(list(range(3,6)))

#args=[3,16,2,9] #TypeError: range expected at most 3 arguments, got 4
args =[2,16,2]
args=(20,200,4)
print(list(range(*args))) #unpacking
print(*args)

d={'a':1,'b':2}
def test(a,b):
    print(a,b)
test(**d)

### Lambda Expressions

def make_incrementor(n):
    return lambda x:x+n

f= make_incrementor(100)
print(f(11))

pairs =[(1,'one'),(2,'two'),(3,'ahree')]

pairs.sort(key=lambda pair:pair[1])

print(pairs)

## Documentation Strings

def my_function():
    """ Do nothing,but document it.
    No,really, it doesn't do anything

    Returns
    -------
    None.

    """

print(my_function.__doc__)

### Function Annotations

def f(ham:str,eggs:str ='eggs')->str:
    print('Annotations:', f.__annotations__)
    print("Arguments:",ham,eggs)
    return ham + ' and '+ eggs

f('spam')




