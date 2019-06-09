
'''*************       List Datatype - []      ***************'''


# Empty List
Course_name = []
print(Course_name)
print(len(Course_name),type(Course_name),id(Course_name))

# list with different elements
course_name1 = ['Python','Devops',"AWS",10,10.50,3+5j,' ', "$"]
            # strings,, int , float, complex , space, special character

print(course_name1)
print(len(course_name1),type(course_name1),id(course_name1))
print ( " ")

# enumerate built in function

print (list(enumerate(course_name1)))
print(enumerate(course_name1))

# indexing in list

print ("")
print(course_name1[0])
print(course_name1[3])
print(course_name1[0:3])
print(course_name1[0:])
print(course_name1[0::2])
print(course_name1[:])

# Negative Indexing
print (" ")
print(course_name1[-1])
print(course_name1[-1::2])
print(course_name1[-1::-2])


'''
o/p - 

[]
0 <class 'list'> 1675206943368
['Python', 'Devops', 'AWS', 10, 10.5, (3+5j), ' ', '$']
8 <class 'list'> 1675206943432
 
[(0, 'Python'), (1, 'Devops'), (2, 'AWS'), (3, 10), (4, 10.5), (5, (3+5j)), (6, ' '), (7, '$')]
<enumerate object at 0x000001860BFCD798>

Python
10
['Python', 'Devops', 'AWS']
['Python', 'Devops', 'AWS', 10, 10.5, (3+5j), ' ', '$']
['Python', 'AWS', 10.5, ' ']
['Python', 'Devops', 'AWS', 10, 10.5, (3+5j), ' ', '$']
 
$
['$']
['$', (3+5j), 10, 'Devops']

'''