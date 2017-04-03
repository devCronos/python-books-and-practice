from collections import defaultdict

"""
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)
"""

d = {} # A regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)

print(d)

from collections import OrderedDict
e = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in e:
    print(key, e[key])

