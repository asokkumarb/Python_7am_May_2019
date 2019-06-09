
# List Method : Sort ( )

'''

sorting list in below order of str

1. Special Characters as str
2. Numbers as str
3.Alphabets - A-Z
4.Alphabets - a-z

- will give error when mixed element of int, Special Character
'''

# acoolList = ['c','t',5,'7',"A"," ","$",25.05,"j",4+5j] - will give error

acoolList = ['c','t','7',"A"," ","$","j",'3.5','5+7j']

onemorelist = [98,65,12,78,96,24,30]

print(acoolList)
print("")

acoolList.sort()
print(acoolList)

'''
o/p -

['c', 't', '7', 'A', ' ', '$', 'j', '3.5', '5+7j']

[' ', '$', '3.5', '5+7j', '7', 'A', 'c', 'j', 't']

'''