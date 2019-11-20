#!/usr/bin/python

x = float(input("Enter the value of x :"))

y = float(input("Enter the value of y :"))

z = float(input("Enter the value of z :"))

if x < y:
    if x < z:
        min = x
    else:
        min = z
else:
    if y < z:
        min = y

print(min)

