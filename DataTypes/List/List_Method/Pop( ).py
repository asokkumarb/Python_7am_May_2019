
# List Method : Pop( )

'''

to remove last element

'''

pydev = ["DevOps","AWS",1985,2019,1985,"devops",2018]

pydev.pop()
print(pydev)
print("")

print(list(enumerate(pydev)))
print("")

pydev.pop(2)
print(pydev)
print("")

pydev.pop(0)
print(pydev)

'''
0/p -
['DevOps', 'AWS', 1985, 2019, 1985, 'devops']

[(0, 'DevOps'), (1, 'AWS'), (2, 1985), (3, 2019), (4, 1985), (5, 'devops')]

['DevOps', 'AWS', 2019, 1985, 'devops']

['AWS', 2019, 1985, 'devops']
'''
