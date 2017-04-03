import re

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

print(mo.group(1))

batRegex = re.compile(r'Bat(wo)?man')
mo3 = batRegex.search('The Adventures of Batman')
print(mo3.group())

mo4 = batRegex.search('The Adventures of Batwoman')
print(mo4.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo5 = phoneRegex.search('My number is 415-555-4242')
print(mo5.group())

mo6 = phoneRegex.search('My number is 555-4242')
print(mo6.group())

print(mo3.group())


greedyHaRegex = re.compile(r'(Ha){3,5}')
mo7 = greedyHaRegex.search('HaHaHaHaHa')
print(mo7.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo8 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo8.group())

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')