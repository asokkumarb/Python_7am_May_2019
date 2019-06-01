# center(width[, fillchar])

''' Returns the string centered in a string of length width. P
adding can be done using the specified
fillchar (the default padding uses an ASCII space).
The original string is returned if width is less than or equal to len(s)
'''


a = "bee"
b = a.center(13, "#")
print(b)