import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

