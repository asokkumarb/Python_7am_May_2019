
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

print(type(tuple1))

print(aTuple[0:3])