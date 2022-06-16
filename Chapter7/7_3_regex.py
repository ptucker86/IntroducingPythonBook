import re
source = 'Young Frankenstein'
m = re.match('You', source)

if m:
    print(m.group())

m = re.search('Frank', source)
if m:
    print(m.group())

text = '''
• . means any single character.
• * means any number of the preceding thing. Together, .* mean any number of
characters (even zero).
• Frank is the phrase that we wanted to match, somewhere.
'''

m = re.match('.*Frank', source)
if m:
    print(m.group())

