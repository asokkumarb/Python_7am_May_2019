"""
# count()

pydev = ["DevOps","AWS",1985,2019,1985,"devops"]

print(pydev.count(1985))

# append()

aws = [10,20,30]

aws.append(40)

print(aws)

aws.append('Build on Cloud')

print(aws)

aws.append(['Movie','Rating','Year'])

print(list(enumerate(aws)))

# del
del aws[5]

print(list(enumerate(aws)))

"""

# extend()

vcs_github = ['Movie','Rating','Year']

raw_data = [10,20,30,40]

print(vcs_github)
print(raw_data)

vcs_github.extend(raw_data)

print(vcs_github)
print(raw_data)

