
# isalnum () Method :

'''

Returns True if all characters in the string are alphanumeric
and there is at least one character special char or space
Returns False otherwise.

'''


str1 = "Fitness"         # alpha char only
print(str1.isalnum())

str2 = "123"             # numeric only
print(str2.isalnum())

str3 = "1.23"            # numeric and special char
print(str3.isalnum())

str4 = "$*%!!!"          # special char
print(str4.isalnum())

str5 = "0.34j"           # specialchar , digits and alpha
print(str5.isalnum())

str6 = "fitness123"      # alpha and numeric
print (str6.isalnum())