
# DataTypes : Dictionaries

'''

A dictionary is a collection which is unordered,
changeable and indexed. In Python dictionaries are written
with curly brackets, and they have keys and values.

# dict{}
# {}
# Key & Value
# Element is seperated with ,
# mutable DataType

'''

d1 = {'firstname' : 'Hardik','Lastname':'Patel','Course':'Python','course_lectures':35}

d2 = {} # empty dictionary
print (d2)
print(len(d1),type(d1),id(d1),)
print("")
print(dict(enumerate(d1))) # will print indexing with only key ( will not print value )

'''
o/p - 
{}
4 <class 'dict'> 2884282124400

{0: 'firstname', 1: 'Lastname', 2: 'Course', 3: 'course_lectures'}

'''