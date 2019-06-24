"""
# matchObject = re.match(pattern=, string=, flags=)

r'expression'
R'expression'

# . (a period)    -- matches any single character except newline '\n'

match_Object = re.match(r'(.*)python', string=line, flags=re.M|re.I)

if match_Object:
    message = match_Object.group()
else:
    message = "Patter Does not exist"

print(f"Searching for Pattern python : {message}")

import re

line = '''
Hi,

Welcome to Python 

World 
by 

PYTHON

Keshav Kummari
'''

search_Object = re.search('Python',line,re.M|re.I)

if search_Object:
    message = search_Object.group()
else:
    message = "Patter Does not exist"

print(f"{message}")

import re

# re.sub(pattern=,repl=,string=,max(),flags=)

data = '2004-959-559 # This is a Phone Number'

num = re.sub(r'#.*$',"",data)

print(f"Phone Number is {num}")

num1 = re.sub(r'\D',"",data)

# \D	Match a nondigit: [^0-9]

print(num1)

import re

text = 'abbaaabbbbaabbbaaabb'

pattern = 'ab'

for match in re.findall(pattern,text):
    print(f"Found Match {match}")
import re

pattern = 'this'

text = 'Does this text match the pattern?'

print(text.index('this'))

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Found "%s" in "%s" from %d to %d ("%s")' % \
    (match.re.pattern, match.string, s, e, text[s:e]))


print(f"Start Index {s}  and End Index {e} in a given {text} {text[s:e]}")

"""

import re

# Lets use a regular expression to match a few date strings.
regex = r"[a-zA-Z]+ \d+"
matches = re.findall(regex, "June 24 August 9 Dec 12",re.M|re.I)

for match in matches:
    # This will print:
    #   June 24
    #   August 9
    #   Dec 12
    print ("Full match: %s" % (match))

# To capture the specific months of each date we can use the following pattern
regex = r"([a-zA-Z]+) \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   June
    #   August
    #   Dec
    print ("Match month: %s" % (match))

# If we need the exact positions of each match
regex = r"([a-zA-Z]+) \d+"
matches = re.finditer(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   0 7
    #   9 17
    #   19 25
    # which corresponds with the start and end of each match in the input string
    print ("Match at index: %s, %s" % (match.start(), match.end()))










