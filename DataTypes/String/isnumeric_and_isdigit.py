
# isnumeric () Method :

'''
Returns True if all characters in the string are numeric characters,
and there is at least one character non-numeric, Returns False otherwise.
'''


str1 = "123" # digit
print(str1.isnumeric())

str2 = u"\u00B2" # unicode
print(str2.isnumeric())

str3 = "1.23" # special character and digits
print(str3.isnumeric())

str4 = "u123" # digit and char
print(str4.isnumeric())

str5 = "Fitness" # strings with alpha
print(str5.isnumeric())

str6 = "$*%!!!"    # special character
print(str6.isnumeric())

'''-------------------------------------------------------------------------------------------------------'''

a = "--"
print(a.center(60,'-'))

'''-------------------------------------------------------------------------------------------------------'''

# isdigit () Method :

'''
Returns True if all characters in the string are 
digits and there is at least one character non-digit 
Returns False otherwise.
'''

is_digit1 = "123" # digit
print(is_digit1.isdigit())

is_digit2 = u"\u00B2" # unicode
print(is_digit2.isdigit())

is_digit3 = "1.23" # digit and specialchar
print(is_digit3.isdigit())

is_digit4 = "u123" # char and digit
print(is_digit4.isdigit())

is_digit5 = "Fitness" # char
print(is_digit5.isdigit())

is_digit6 = "$*%!!!"   # special char
print(is_digit6.isdigit())