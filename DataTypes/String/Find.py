
# find () Method :

'''

Will not give error as in index() Method. It will give -1 if condition will false

'''

      # 0123456789
str1 = "This is Python online course"
str2 = "is"

print(str1.find(str2,0))
print (str1.find(str2,4))
print (str1.find(str2,4,20))  # full syntax
print(str1.find(str2,6))
print(str1.find(str2,10,0)) # back counting is now allowed. will give -1 as False