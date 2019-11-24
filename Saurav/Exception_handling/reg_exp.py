import re

"""
line = 'python Welcome to Python world python'

match_obj =re.match(r'Python(.*)',line, re.M|re.I)

if match_obj:
    message =match_obj.group()
else:
    message ="Patern does not exit"

print(message)

"""
"""
import re

pattern = 'this'

text = 'Does this text match the pattern?'

print(text.index('this'))

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Found "%s" in "%s" from %d to %d ("%s")' % \
    (match.re.pattern, match.string, s, e, text[s:e]))

print(f'start index is {s} and end index is {e} in a given "{text}" {text[s:e]}')
"""





