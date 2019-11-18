"""
a = {"emp_id":18061, "first_name":"saurav", "middel_name":"kummar", "last_name" :"dash"}
print(a)

print(dict(enumerate(a)))

a["middel_name"]= "ranjan"

print(a)

a["company"]='syniverse'

print(a)

del a["emp_id"]

print(a)

print(a.keys())
print(a.values())
print(a.items())

"""
'''
a = {"emp_id":18061, "first_name":"saurav", "middel_name":"kummar", "last_name" :"dash"}

b = ("emp_id", "name", "company")

print(dict.fromkeys(b,50))

'''
a = {"emp_id":18061, "first_name":"saurav", "middel_name":"kummar", "last_name" :"dash"}

print(a.setdefault("middel_name","ranjan"))

print(a.setdefault("course","python"))

print(a)


