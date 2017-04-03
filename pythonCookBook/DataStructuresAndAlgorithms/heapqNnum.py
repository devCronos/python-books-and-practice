from heapq import *
import random

grades = []

for i in range(12):
    x = random.randint(1, 10)
    grades.append(x)

print(grades)
print(nsmallest(4,grades))
print(nlargest(4,grades))

portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = nlargest(3, portfolio, key=lambda s: s['price'])

print(cheap)
print(expensive)