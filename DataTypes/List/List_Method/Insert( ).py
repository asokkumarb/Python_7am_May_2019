
# List Method : insert()

'''

to add element at specific index point

'''

pydev = ["DevOps","AWS",1985,2019,"devops",2018]

India = ['Virat','Parthiv','Chahal']

print (list(enumerate(pydev)))
print("")

pydev.insert(0,"language")
print(pydev)
print("")

pydev.insert(-1,15)
print(pydev)
print("")

# pydev.insert("Bharat")  - will give error as syntax rules not follow .insert(index,element)

'''
o/p -
[(0, 'DevOps'), (1, 'AWS'), (2, 1985), (3, 2019), (4, 'devops'), (5, 2018)]

['language', 'DevOps', 'AWS', 1985, 2019, 'devops', 2018]

['language', 'DevOps', 'AWS', 1985, 2019, 'devops', 15, 2018]
'''
