"""
A Tuple is an immutable sequence of values of any type
tuple()
'','',''," ",
Elements will start with 0th index
list[]
"""

aTuple = ('Python',"Linux",'''AWS''',"""Azure""",10,20.75,3+5j)

tuple1 = 'Python',"Linux",'''AWS''',"""Azure""",10,20.75,3+5j

print(type(aTuple),id(aTuple),len(aTuple),tuple(enumerate(aTuple)))
print("")

print(type(tuple1))
print("")

print(aTuple[0:3])
print("")

print(aTuple[2])
print("")

print(aTuple[-1])
print("")

print(aTuple[0:])
print("")

'''
o/p
<class 'tuple'> 2728876663688 7 ((0, 'Python'), (1, 'Linux'), (2, 'AWS'), (3, 'Azure'), (4, 10), (5, 20.75), (6, (3+5j)))

<class 'tuple'>

('Python', 'Linux', 'AWS')

AWS

(3+5j)

('Python', 'Linux', 'AWS', 'Azure', 10, 20.75, (3+5j))
'''