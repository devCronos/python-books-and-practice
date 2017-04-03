import re

# \d Any numeric digit from 0 to 9.
# \D Any character that is not a numeric digit from 0 to 9.
# \w Any letter, numeric digit, or the underscore character.
# (Think of this as matching “word” characters.)
# \W Any character that is not a letter, numeric digit, or the
# underscore character.
# \s Any space, tab, or newline character. (Think of this as
# matching “space” characters.)
# \S Any character that is not a space, tab, or newline.)

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, '
                        '7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
#Making my own regex character class
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello world!')

print(beginsWithHello.search('He said hello.') == None)

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')

print(endsWithNumber.search('Your number is forty two.') == None)


wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')

print(wholeStringIsNum.search('12345xyz67890') == None)

print(wholeStringIsNum.search('12 34567890') == None)

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())

print(robocop.search('ROBOCOP protects the innocent.').group())

print(robocop.search('Al, why does your programming book talk about robocop so much?').group())