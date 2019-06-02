#!/usr/bin/python
       #01234567891011   Left to Right
       #-11-10-9-8-7-6-5-4-3-2-1  Right to Left

str1 = "Hello World!"  # 11 characters

str2 = 'This is an example string'
       #01234
       #1 2 3 4 5 6 7 8 9
#str2 = "102030405060708090"

print(str1[0])    # (Indexing) Calling First Index from Left to Right Indexing
print(str1[-1])   # (Indexing) Calling First Index from Right to Left Indexing
print (str1[2:7])  # Range Slice Start index : end index-1
print (str1[:5])   # Calling until 4th index
print(str1[0:])
print(str1[:])

print (str2[0::4]) # Zero Based Indexing
print (str2[0::3])

print ((str1 + " ")* 3)   # Repetation
print ("updated string ", str1[:6] + "planet")  # Concatenation
print ("updated string ", str1[:12] + "Perl")



