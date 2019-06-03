#!/usr/bin/python

"""
#!/usr/bin/python

# 1. capitalize() Method :

# Note: string with only its first character capitalized.

a01 = "welcome to python world"
a02 = "python world"
a03 = "to python world"

print ("a01.capitalize() : ", a01.capitalize(),id(a01),type(a01),len(a01))
print("")
print ("a02.capitalize() : ", a02.capitalize(),id(a02),type(a02),len(a02))
print("")
print ("a03.capitalize() : ", a03.capitalize(),id(a03),type(a03),len(a03))

#!/usr/bin/python

       #012345678910
str1 = "this abc is really a string example....wow!!!"

str2 = "is"

print (str1.find(str2))
print (str1.find(str2, 0, 10))
print (str1.find(str2, 10, 30))



"""
27	rfind(str, beg=0,end=len(string))
	Same as find(), but search backwards in string.
"""
print (str1.rfind(str2))
print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2, 10, 40))

#!/usr/bin/python

      # 0123456
str1 = "this is string example....wow!!!"
str2 = "is"

print (str1.rindex(str2))
print (str1.index(str2))

"""
28	rindex(str, beg=0, end=len(string))
	Same as index(), but search backwards in string.
"""
#!/usr/bin/python

str = "Python0007"

print(len(str))

print (str.rjust(20, '*'))

print (str.ljust(25, '#'))

"""
29	rjust(width,[, fillchar])
	Returns a space-padded string with the original
	string right-justified to a total of width columns.
"""

#!/usr/bin/python

str = "THIS IS STRING EXAMPLE....WOW!!!" 
print (str.isupper())

str = "THIS is string example....wow!!!"
print (str.isupper())

"""
17	isupper()
	Returns true if string has at least one cased character and all
	cased characters are in uppercase and false otherwise.
"""

#!/usr/bin/python

_Iphone7 = "Linux Unix Perl Python And Django...Etc!!!"
print (_Iphone7.istitle())

_iphone8 = "Linux unix perl python and django...etc!!!"
print (_iphone8.istitle())

"""
16	istitle()
	Returns true if string is properly "titlecased"
	and false otherwise.
"""


#!/usr/bin/python

_01_ = "  "
print (_01_.isspace())

_02_ = "Linux Unix"
print (_02_.isspace())

_03_ = "Linux Unix Perl Python and django...etc!!!"
print (_03_.isspace())

"""
15	isspace()
	Returns true if string contains only whitespace
	characters and false otherwise.
"""

#!/usr/bin/python

_007 = u"$6"
print (_007.isnumeric())

_008 = u"786786"
print (_008.isnumeric())

_008 = "786786"
print (_008.isnumeric())


_009 = "03948274"  # Only digit in this string
print (_009.isdigit())

_006 = "Linux Unix Perl Python and django...etc!!! 0009"
print (_006.isdigit())

"""
14	isnumeric()
	Returns true if a unicode string contains only numeric
	characters and false otherwise.
"""

#!/usr/bin/python

rossum = "Python with django framework!"

print(rossum.islower())

rossum = "Linux Unix Perl Python and django...etc!!!"

print (rossum.islower())

"""
13	islower()
	Returns true if string has at least 1 cased character and all cased
	characters are in lowercase and false otherwise.
"""

#!/usr/bin/python

str = "THIS IS STRING EXAMPLE....WOW!!!"
print (str.isupper())

str = "Tthi is string example....wow!!!"
print (str.isupper())

"""
17	isupper()
	Returns true if string has at least one cased character and all
	cased characters are in uppercase and false otherwise.
"""


#!/usr/bin/python

str = "2020"  # No space in this string

print(str.isdigit())

str = "01992992"

print (str.isdigit())


"""
12	isdigit()
	Returns true if string contains only digits and false otherwise.

"""	

#!/usr/bin/python
 
str_alpha = "this" # Only String

alpha_space = "this "  # String with Space

alpha_specialChar = "this *" # String with Special Char

str_digits = "this007"  # No space & digit in this string

print(str_alpha.isalpha())

print(alpha_space.isalpha())

print(alpha_specialChar.isalpha())

print(str_digits.isalpha())

rossum = "Pythonandperllinux"

print (rossum.isalpha())

"""
11	isalpha()
	Returns true if string has at least 1 character and all
	characters are alphabetic and false otherwise.
"""

#!/usr/bin/python

"""
27	rfind(str, beg=0,end=len(string))
	Same as find(), but search backwards in string.
"""

str1 = "Python number string examples"

str2 = "num"

print (str1.find(str2)) # Looking for index 

print (str1.find(str2, 10)) # Start index 10

print (str1.find(str2, 0,10)) # Start and ending index i.e. 15,20

#!/usr/bin/python
      # 01234
str1 = "Its python world....wow!!!"
str2 = "python"

print (str1.index(str2))

print (str1.index(str2, 0))

print(len(str1))

print (str1.index(str2, 0,20))

"""
9	index(str, beg=0, end=len(string))
	Same as find(), but raises an exception if str not found.
"""

#!/usr/bin/python

str = "Welcome to python world"

sub = "o"

print("Varify the substring", str.count(sub),len(str))

print("Varify the substring from a specific index ", str.count(sub, 10, 23))

sub1 = "python"
print ("str.count(sub1) : ", str.count(sub1))







#!/usr/bin/python

title_1 = "variables datatypes numbers list tuples dictionaries sets"

print(title_1)

print (title_1.title())

print(title_1)


simpleData = " & "

sequence = ("a", "b", "c")

print(simpleData,type(simpleData),id(simpleData),len(simpleData))

print(sequence,type(sequence),id(sequence),len(sequence))

# join(sequence)

print(simpleData.join(sequence))

#a & b & c &

joiner = "-"
title = "Python World By Guido Van Rossum"

print(joiner.join(title))

P-y-t-h-o-n- -W-o-r-l-d- -B-y- -G-u-i-d-o- -V-a-n- -R-o-s-s-u-m



# Replace Method

# replace(old,new[,max])

dataValues = "Python is a Programming and is Scripting is Language"

print(dataValues.replace("is","was"))
print(dataValues.replace("is","WAS",2))

# Strip Method : Removes all trailing whitespace of string

DataScience = "%%DataMining and DataFilter%%"

print(DataScience.strip("%"))

print(DataScience.lstrip("%"))

print(DataScience.rstrip("%"))

# split Method

realData = "ABC123 ABC123 ABC123 ABC123"

print(realData.split())
print(realData.split("ABC"))
print(realData.split("123"))


# StartsWith & EndsWith Method

a = "Python was created by Guido Van Rossum"

print(a.startswith("was"))
print(a.startswith("python"))
print(a.startswith("Python"))

print(a.endswith("Van"))
print(a.endswith("Rossum"))



Built-in Functions:

abs()	dict()	help()	min()	setattr()
all()	dir()	hex()	next()	slice()
any()	divmod()	id()	object()	sorted()
ascii()	enumerate()	input()	oct()	staticmethod()
bin()	eval()	int()	open()	str()
bool()	exec()	isinstance()	ord()	sum()
bytearray()	filter()	issubclass()	pow()	super()
bytes()	float()	iter()	print()	tuple()
callable()	format()	len()	property()	type()
chr()	frozenset()	list()	range()	vars()
classmethod()	getattr()	locals()	repr()	zip()
compile()	globals()	map()	reversed()	__import__()
complex()	hasattr()	max()	round()
delattr()	hash()	memoryview()	set()


# lower() upper() & swapcase()

lowercase_alphabets = "abcdefghijkLMNOpqrstuvwxyz"

print(lowercase_alphabets)

print(lowercase_alphabets.upper())

uppercase_alphabets = "ABCDEFGHIJKlmnoPQRSTUVWXYZ"

print(uppercase_alphabets)

print(uppercase_alphabets.lower())

name = "GuiDO"

print(name.swapcase())

"""

