"""
1. Required Arguments

2. Keyword Arguments

3. Default Arguments

&

4. Variable-Length Arguments

# 1. Required Arguments

# Creating of a Function
def hello(a):
    print(a)


# Creating of a Variable
abc = 'Welcome to PyWorld'

# Accessing/Calling of a Function
hello(abc)

# hello(10)
# hello('Welcome to PyWorld')

# 2. Keyword Arguments

def data(name,age):
    print(f"Name : {name}")
    print(f"Age  : {age}")
    return

data(name="Guido Van Rossum",age=50)

# 3. Default Arguments

def data(name, age = 35):
    print(f"Name : {name}")
    print(f"Age  : {age}")
    return

data(name="Amazon")

"""

# 4. Variable-Length Arguments

def info(*vartuple):
    #print(var1)

    for i in vartuple:
        print(i)
    return

info(10,20,30,40,50,60,70,80,90)
