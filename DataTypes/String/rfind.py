
# rfind () Method :

'''

it will check string from last index to first index
rindex = reverse index
'''

str1 = "This is Python online course. is starting from today"
str2 = "is"

print(str1.rfind(str2,0))
print (str1.rfind(str2,4))
print (str1.rfind(str2,4,20))   # # full syntax
print(str1.rfind(str2,6))
print(str1.rfind(str2,10,0)) # back counting is now allowed. will give -1 as False