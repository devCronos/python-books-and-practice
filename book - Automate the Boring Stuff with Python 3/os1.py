import os


print(os.getcwd())
os.chdir('E:\\new folder')
print(os.getcwd())
os.chdir('.\\abk')
print(os.getcwd())

# for i in range (10):
#     for j in range (10):
#         os.makedirs('.\\{}\\{}'.format({i},{j}))
print(os.path.abspath('.\\{3}\\{5}'))
print(os.path.relpath('.\\{3}\\{5}'))
print(os.path.relpath('C:\\Windows', 'C:\\'))

path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))

print(os.path.dirname(path))

# calcFilePath = 'C:\\Windows\\System32\\calc.exe'
# print(os.path.split(calcFilePath))
#
# print((os.path.dirname(calcFilePath), os.path.basename(calcFilePath)))
# print(calcFilePath.split(os.path.sep))
#
# print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
#
# print(os.listdir('E:\\dld'))
#
# totalSize = 0
# for filename in os.listdir('E:\\dld'):
#     totalSize = totalSize + os.path.getsize(os.path.join('E:\\dld', filename))
# print(totalSize)

os.path.exists('C:\\Windows')

print(os.path.exists('C:\\some_made_up_folder'))
print(os.path.isdir('C:\\Windows\\System32'))
print(os.path.isfile('C:\\Windows\\System32'))
print(os.path.isdir('C:\\Windows\\System32\\calc.exe'))
print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))