
# isspace () Method :

'''

Returns True if there are only whitespace characters
in the string and there is at least one character.
Returns False otherwise.
'''

str_space = "  " # only space

space_char = "python  " # space and character

space_char_special = " abc #';"

print (str_space.isspace())
print(space_char.isspace())
print(space_char_special.isspace())
