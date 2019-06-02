
# index () Method :

'''
To check small string is substring of main string.
( from first index to last index )

if substring will not find in main string then, condition will become false and
it will give error unlike find () and rfind () method
'''

str1 = "This is Python online course. is starting from today"
str2 = "is"

print(str1.index(str2,0))
print (str1.index(str2,4))
print (str1.index(str2,4,20))   # full syntax
print(str1.index(str2,6))
print(str1.index(str2,10,0)) # back counting is now allowed. will give error