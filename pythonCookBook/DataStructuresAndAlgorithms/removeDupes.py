#If the values in the sequence are hashable, the problem can be easily solved using a set
#and a generator. For example:
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
#Here is an example of how to use your function:
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))