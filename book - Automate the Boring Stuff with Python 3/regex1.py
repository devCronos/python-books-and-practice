import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

phoneNumRegex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1 = phoneNumRegex1.search('My number is 415-555-4242.')
print(mo1.group(1),

mo1.group(2),

mo1.group(0),

mo1.group())

print(mo1.groups())

areaCode, mainNumber = mo1.groups()
print(areaCode)

print(mainNumber)