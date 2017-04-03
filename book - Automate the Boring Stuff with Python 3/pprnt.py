import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))

fileObj = open('myCats.py', 'w')
print(fileObj.write('cats = ' + pprint.pformat(cats) + '\n'))

fileObj.close()

