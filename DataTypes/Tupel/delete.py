
# Tuple Method : Delete

'''
tuple object doesn't support item deletion
'''

tup1 = ('python', 'aws', 'azure', 1990, 20.75)

print(tuple(enumerate(tup1)),id(tup1),len(tup1),type(tup1))

 # del tup1[1]

'''error : TypeError: 'tuple' object doesn't support item deletion '''

del tup1

print (tup1)

'''
o/p -
NameError: name 'tup1' is not defined 

as it has been deleted 
'''