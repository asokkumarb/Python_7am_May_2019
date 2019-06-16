
# tuple Method : min and maz

'''

apply to only strings tuple or only to int
does not support mix tuple
does not support complex and int


'''

tup1 = ('python','online','training')

tup2 = (12,12.5,15)

tup3 = ('python','online','training',12,12.5,15)

print("Min Value element : ", min(tup1))
print("Max Value element : ", max(tup1))
print("")
print("Min Value element : ", min(tup2))
print("Max Value element : ", max(tup2))

'''
print("Min Value element : ", min(tup3)) 
print("Max Value element : ", max(tup3))

TypeError: '<' not supported between instances of 'int' and 'str'

# doesn't support int and str

'''
'''
o/p - 

Min Value element :  online
Max Value element :  training

Min Value element :  12
Max Value element :  15


'''