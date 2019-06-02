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


# formatting of strings

print ("Your name is %s and your account id is %d" %("Kevin",14456))
print ("Calling str1 {0} and calling str2 {1}".format(str1,str2))
print ("Value1 {} Value2 {} and Value3 {}".format("python",100,"pycharm"))
print ("Value1 {1} Value2 {0} and Value3 {2}".format("python",100,"pycharm"))
print ("Value1 {a} Value2 {b} and Value3 {c}".format(a="python",b=100,c="pycharm"))
