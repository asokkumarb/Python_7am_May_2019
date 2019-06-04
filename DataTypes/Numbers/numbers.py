#!/usr/bin/python

"""
Python Supports Integers, Floating & Complex Data.

They are defined as int, float & complex class in Python

"""

raw_data = 5  #Integers

print(raw_data,type(raw_data),id(raw_data))

float_data = 5.75 #Floating

print(type(float_data),id(float_data))

acomplex_data = 4 + 5j #Complex

print(acomplex_data,type(acomplex_data),id(acomplex_data))

print(isinstance(acomplex_data, complex))

print(isinstance(float_data, complex))

print(isinstance(float_data, float))

print(isinstance(raw_data, int))

# Built-in Functions in Numbers DataTypes:

# 1. int()
# 2. float()
# 3. complex()

# Mathematical Functions :

'''
1. +    : Plus
2. -    : Minus
3. /    : Slash
4. *    : Asterisk
5. %    : Percent
6. <    : Less-Than
7. >    : Greater-than
8. <=   : Less-than-or-equal
9. =>   : Greater-than-or-equal
'''

# Built-in Methods

# 1. abs()  : 0-9 (The Positive Distance between n and zero

print(abs(-30))

# 2. ceil() : The smallest integer not less than x value

import math

print(math.ceil(61.1))
print(math.ceil(-61.1))

import awscli

awscli.EnvironmentVariables()

import azure
