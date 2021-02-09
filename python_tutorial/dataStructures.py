#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:15:29 2021

@author: dzgygmdhx
"""

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(type(fruits))

fruits.append('jiaozi')
fruits.extend(('a','b'))
fruits.sort()


print(fruits)

## Using Lists as Stacks

stack = [3, 4, 5]

stack.extend((6,7,8))

stack.append(9)

print(stack)

print(stack.pop())
print(stack)

## Using Lists as Queues  first in first out
 
from collections import deque

queue = deque(fruits)

print(queue.count('apple'))

queue.append("charlie")

print(queue)

print(queue.popleft())

## List Comprehensions

squares=[]

for x in range(10):
    squares.append(x**2)

print(squares)

squares1= list(map(lambda x: x**2, range(10)))
print(squares1)

squares2=[x**2 for x in range(10)]
print(squares2)

someSet =[(x,y) for x in [1,2,3] for y in[10,20,30] if x!=y]
print(someSet)

vec = [-4, -2, 0, 2, 4]

double_vec = [x*2 for x in vec]

postive_vec = [x for x in vec if x>=0]

abs_vec = [abs(x) for x in vec]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']

strip_freshfruit = [fruit.strip() for fruit in freshfruit]

createATuple=[(x,x**2) for x in vec]

vec = [[1,2,3], [4,5,6], [7,8,9]]
flatVec1 = [elem for elem in vec]
print(flatVec1)
flatVec2 = [num for num in flatVec1]
print(flatVec2)

## kind of difficult
flatVec3= [num for elem in vec for num in elem]

flatVec4= [num for elem in vec for num in elem]


print(flatVec3)
print(flatVec4)

from math import pi
piDemo=[str(round(pi,i)) for i in range(1,6)]
print(piDemo)



# print(double_vec)
# print(postive_vec)
# print(abs_vec)
# print(strip_freshfruit)
# print(createATuple)


### Nested List Comprehensions

matrix =[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    ]

#              first for                  second for
transpose1 = [ [row[i] for row in matrix] for i in range(4) ]
# transpose2 = [ (r[i] for r in matrix) for i in range(4) ]
transpose2 = [ [r[i] for r in matrix] for i in range(4) ]
print(transpose1)
print(transpose2)

transposed=[]

# first for
for i in range(4):
    transposed.append([row[i] for row in matrix]) # second for
    print(transposed)
    
print(transposed)

## which in turn is the same as:
# then we can how simple and directily use 
# [[row[i] for row in matrix] for i in range(4)]
transposedd=[]

for i in range(4):
    transposedd_row=[]
    for row in matrix:
        transposedd_row.append(row[i])
    transposedd.append(transposedd_row)

print(transposedd)

# * operator can unpack the arguments out of a list or tuple
zipFunction =list(zip(*matrix))

print(zipFunction)

### The del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]

del a[3:5]
print(a)

del a

# print(a)

###  Tuples and Sequences

t = 1234,5423,'nihao',[1,2,(22)],(1,24,'dd')

print(type(t)) #<class 'tuple'>

u= t,'charlie'

print(u)

# Tuples is immutable

#TypeError: 'tuple' object does not support item assignment
# u[1]="d"

# Tuples can contain mutable objects, 
u[0][3].append(1909)

print(u)

empty=()
print(len(empty))

singleton='hello',

print(len(singleton))

tt= 1,2,3
# Multiple assignment is really just a combination of tuple packing and sequence unpacking
x,y,z = tt

print(x+y+z)

## Sets Curly braces or the set() function  both can be used to create sets 

basket ={'apple','orange','apple','pear'}

print(basket)#{'pear', 'apple', 'orange'}

emptySet= set()
emptyDic={}

# <class 'dict'>
# <class 'set'>
print(type(emptyDic))

print(type(emptySet))

print('pear' in basket)

a= set('abracadabra')
# TypeError: set expected at most 1 argument, got 2
# aa= set('abcda','b')

b = set('alacazam')

print(a-b) # in a but not in b

print(a| b) # in a or b or both

print(a & b) # in  both a and b

print(a ^b) # letters in a or b but not both

# print(aa)
print(a)

a= {x for x in 'abscedfrfea' if x not in'abc'}

print(a)

### Dictionaries

tel = {'jack':4098, 'sape':4139}

tel['charlie']=8889

print(tel)

print(tel['jack'])

del tel['jack']

print(tel)

dicToList = list(tel)
print(dicToList)

print('sape' in tel)
 
newDic = dict([('a',1),('b',90),(99,'dddd')])

print(newDic)

newDic2= {x: x**2 for x in (2,4,6)}

print(newDic2)

newDic3 = dict(a1=1,b2=2,b3=3)

print(newDic3)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k,v in knights.items():
    print(k,v)
    
for index,v in enumerate(['tic','ddd','tig']):
    print(index,v)

for index,v in enumerate(('tic','ddd','tig')):
    print(index,v)


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q,a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q,a))
    

for i in reversed(range(1,10,2)):
    print(i)
    
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for i in sorted(basket):
    print(i)
    
# 1: romove duplicate 2: orderd
for f in sorted(set(basket)):
    print(f)

# it is sometimes temping to change a list while you are looping over it;however,it
# is often simpler and safer to create a new list instead.

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]

filtered_data=[]

for i in raw_data:
    if not math.isnan(i):
        filtered_data.append(i)

### More on Conditions
# while if
# in not in
# is is not
# and or

### Comparing Sequences and Other Types
# (1, 2, 3)              < (1, 2, 4)
# [1, 2, 3]              < [1, 2, 4]
# 'ABC' < 'C' < 'Pascal' < 'Python'
# (1, 2, 3, 4)           < (1, 2, 4)
# (1, 2)                 < (1, 2, -1)
# (1, 2, 3)             == (1.0, 2.0, 3.0)
# (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)


