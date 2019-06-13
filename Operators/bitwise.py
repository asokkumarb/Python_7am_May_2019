#!/usr/bin/python3

a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101

print ('a=',a,':',bin(a),'b=',b,':',bin(b))

c = 0

c = ~ a

print(c, bin(c))

c = a << 2

print(c, bin(c))

c = a >> 2

print(c, bin(c))