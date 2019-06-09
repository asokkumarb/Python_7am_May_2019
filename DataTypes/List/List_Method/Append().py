
# List Method : Append()

'''

add element to list at

'''

pydev = ["DevOps","AWS",1985,2019,"devops",2019]

print(pydev)
print("")

pydev.append(33)   #  adding number on list
print(pydev)
print("")

pydev.append('India')   #  adding string on list
print(pydev)
print("")

pydev.append(['Australia','England','South Africa']) # adding list on list  bg
print(pydev)
print ("")


'''
o/p - 

['DevOps', 'AWS', 1985, 2019, 'devops', 2019]

['DevOps', 'AWS', 1985, 2019, 'devops', 2019, 33]

['DevOps', 'AWS', 1985, 2019, 'devops', 2019, 33, 'India']

['DevOps', 'AWS', 1985, 2019, 'devops', 2019, 33, 'India', ['Australia', 'England', 'South Africa']]

'''



