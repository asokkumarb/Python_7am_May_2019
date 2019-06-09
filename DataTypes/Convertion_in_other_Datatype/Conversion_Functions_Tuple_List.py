
# conversion from list to tupel

aList = ['FirstName','LastName',"Guido","Rossum",10,20]

print(aList,type(aList))

a = tuple(aList)

print(a,type(a))

# conversion from tupel to list

abc = ('FirstName', 'LastName', 'Guido', 'Rossum', 10, 20)

c = list(abc)

print(list(c),type(c))

'''
o/p -
['FirstName', 'LastName', 'Guido', 'Rossum', 10, 20] <class 'list'>
('FirstName', 'LastName', 'Guido', 'Rossum', 10, 20) <class 'tuple'>
['FirstName', 'LastName', 'Guido', 'Rossum', 10, 20] <class 'list'>
'''