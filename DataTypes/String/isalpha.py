
# isalpha () Method :

'''
Returns True if all characters
in the string are alphabetic and
there is at least one character non alphabetic,
Returns False otherwise.
'''


str1_alpha = "python" # only string

alpha_space = "python " # string with space

alpha_specialchar = "python #" # string with Special Character

alpha_digit = "python123" # string with number

digit = "123" # only digits

special = "#'['" # only special character

print (str1_alpha.isalpha())
print (alpha_space.isalpha())
print(alpha_specialchar.isalpha())
print (alpha_digit.isalpha())
print(digit.isalpha())
print(special.isalpha())