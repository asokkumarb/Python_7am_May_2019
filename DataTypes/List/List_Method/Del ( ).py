
# List Method : Del ()

'''

use to delete element from list or full list

'''

pydev = ["DevOps","AWS",1985,2019,"devops",2019]
print (list(enumerate(pydev)))
print ("")

del pydev[2]   # delete 2nd index element
print (pydev)
print(list(enumerate(pydev)))
print ("")

del pydev[-1]  # delete last index element
print (pydev)

del pydev
# print (pydev)   - will give error as pydev has been deleted on last command

'''
o/p - 
[(0, 'DevOps'), (1, 'AWS'), (2, 1985), (3, 2019), (4, 'devops'), (5, 2019)]

['DevOps', 'AWS', 2019, 'devops', 2019]
[(0, 'DevOps'), (1, 'AWS'), (2, 2019), (3, 'devops'), (4, 2019)]

['DevOps', 'AWS', 2019, 'devops']

'''