a = ["python", "aws", "devops", 5, 10.5, 3+2j, "$"]

print(a.count("cloud"))

b = [20, 30, 50]

b.append(["adding somthing", 40, 50])

print(b)

print(list(enumerate(b)))


del b[2]

print(b)

print(list(enumerate(b)))

a.extend(b)

print(a)

