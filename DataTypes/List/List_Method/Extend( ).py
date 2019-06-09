
# List Method : Extend( )

'''

to extend list with other list

'''

India = ['Virat','Parthiv','Chahal']

Australia_england = ['Michel','Stoinis','Ali']

India.extend(Australia_england)
print("")

Australia_england_number = [3]
# Australia_england_number = 3  # will give error as not iterable

India.extend(Australia_england_number)
print(India)
print("")

Australia_england.extend(India)
print(Australia_england)

'''
o/p -

['Virat', 'Parthiv', 'Chahal', 'Michel', 'Stoinis', 'Ali', 3]

['Michel', 'Stoinis', 'Ali', 'Virat', 'Parthiv', 'Chahal', 'Michel', 'Stoinis', 'Ali', 3]
'''




