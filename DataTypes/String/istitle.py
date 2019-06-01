
# istitle () Method :

'''

Returns True if the string is a titlecased string and
there is at least one character
(for example uppercase characters may only follow
uncased characters and lowercase characters only cased ones).

Returns False otherwise

'''

str1 = "We Are Learning Python Basics" # Each word titlecase

str2 = "We are learning python basics" # first word titlecase

str3 = "we are learning python basics" # no titlecase word

str4 = "we are Learning python basics" # middle word titlecase

print(str1.istitle())
print(str2.istitle())
print(str3.istitle())
print(str4.istitle())
