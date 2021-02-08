#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:13:37 2021

@author: dzgygmdhx
"""
# print(2+2)
# print(8/3)
# print(17//3)
# print(17%3)
# print(5**2)
width =20
height= 3*9
print(width * height)

# begin string  '' " " \  \n  r

print('I like "you", but "you" do not like me')
print("I like 'you', but 'you' do not like me")

print('I like \'you\', but  "you" do not like me')

print('I like \'you\', but \'you\' do not like me')

print('I like "you",\nbut "you" do not like me')
print('I like "you",\n   but "you" do not like me')
print(r'I like "you",\nbut "you" do not like me')
print(r'c:\some\home')

#string multiple lines
# End of lines are automatically included in the string, you can use a 
# \ at the end of the line to avoid this
print("""\
      i like you?
      yes i like you
      really?
      sure
      you can see, it is very easy way to do it 
      """
      )
    
print("hello " *3 + 'python world' + 'good!'*2)
print("hello " *3 , 'python world' , 'good!'*2)
# Two or more string literals (i e the ones enclosed between quotes)
# This is only works with two literals though,not with variables or expressions:
print('a' 'b')
print('i like you so much'
      'you ?'
      ' are you sue? ')

word ="Python"
print(word[0])

# for i in word:
    # print(i)

# for (index,i) in word:
#     print(index)
#     print(i)


# +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1


print(word[-1])

# String  inner string [] , index, slicing are all support

print(word[1:2])

print(word[:6])

# [start:end] 
print(word[:2]) # index 0 1 start: 0
print(word[:-2]) # index -6 -5 -4 -3 start: -6
print(word[-5:-2]) #index -5 -4 -3 

# use index  when  too large will get error but use slice ,no error

print(word[:1000])
# pirnt(word[1000]) #  no 

# String in python is immutable 

print(type(word))
# 'str' object does not support item assignment
# word[1]='ddd'

print(type(1))
print(type(None))

print(type(True))

# List in python

squares=[1,4,9,16,25]

print(squares[:3])
squares[0] =1000  # list mutalbe

print(squares[:3])

print(squares[:3]+[10,20])

# TypeError: can only concatenate list (not "int") to list
# print(squares[:3]+10)

print(type(squares))
squares.append(10)
print(squares)


print(squares[:3] +[(1,2)])

squares[:-3] =[1979,1980]

print(squares)

squares[:] =[]


print(squares)

# <class 'builtin_function_or_method'>
print(type(len))

print(len(squares))

# list can be nest and can hold any class type

nestList=[1,[2,3],(2,3),{'dd':'ddd'}]
print(nestList)

# First Steps Towards Programming
# demonstrating that the expression on the rihgt-hand side are all evaluated first
# before any of the assignment take place. The right-hand side expression are evaluated
# from the left to the right

a,b,c =0,1,0
while a<10:
    print(a)
    print(c)
    a,b,c = b,a+b,c+b+a+b

    









