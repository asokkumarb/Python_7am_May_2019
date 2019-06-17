"""
For loop 

for expression in var:
    statements
 
count = 0

name = input("Enter your name : ")

for letter in name:
    if letter in ['A','E','I','O','U','a','e','i','o','u']:
        count = count + 1

print("You have",count,"Vowels in your name")
    
# range(1,11) end-1 10

num = 10

for i in range(1,11):
    print(num,'x',i,'=',num*i)    
"""
#name = input("Enter a Name: ")

#print(len(name))

"""
for i in name:
    print(i)
"""

#!/usr/bin/python

var=input("Enter a String: ")

for letter in var:
    if(letter==' '):
        break
    else:
        print(letter)