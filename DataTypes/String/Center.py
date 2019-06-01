# center() Method :

''' Returns the string centered in a string of length width.
Padding can be done using the specified
fillchar (the default padding(filler) uses an space).

The original string is returned if width is less than or equal to len(s)

Syntax : str.center(width,fillchar)

width -- This is the total width of the string
fillchar -- This is the filler character.

'''


str1 = "HARDIK"
str2 = """PATEL \
HARDIK \
INDRAVADANBHAI\
"""

print ("lenght of str1 :",len(str1))
print ("Ans of str1.center(17,'*') is : ",str1.center(17,'*'))
print (" ")
print ("length of str2 : ",len(str2))
print ("Ans of str2.center(32,'#') is : ",str2.center(32,'#'))
print("")
print ("Ans of str1.center(4,'@') is : ",str1.center(4,'@')) # o/p will be sting itself as new string len is less than original string
