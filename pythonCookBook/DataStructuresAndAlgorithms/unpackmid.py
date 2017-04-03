# *unpacking is naz

import random

grades = []

for i in range(12):
    x = random.randint(1, 10)
    grades.append(x)

print(grades)

def avg(numbers):
    return sum(numbers)/len(numbers)
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

print(drop_first_last(grades))

def first_nine(grades):
    *first_n, last = grades
    return avg(first_n)
print(first_nine(grades))

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
    ]
def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)