import os

# path = os.path.join('usr', 'bin', 'spam')
# print(path)

# myFiles = ['example.csv', 'unencrypted.pdf', 'meetingminutes.pdf']
# for filename in myFiles:
#     print(os.path.join('/home/safety', filename))

# THE CURRENT WORKING DIRECTORY
# cwd = os.getcwd()
# print(cwd)

# new_cwd = os.chdir('/home/safety/Python-Projects')
# new_cwd1 = os.getcwd()
# print(new_cwd1)

# CREATING NEW DIRECTORIES

# mkd = os.makedirs('/home/safety/Python_Projects_Scripts/')
# print(mkd)

# path = os.path.abspath('./Scripts')
# path1 = os.path.isabs('.')
# path2 = os.path.isabs(os.path.abspath('.'))
# print(path2)
# print(path)
# print(path1)

# print only relative path
relative_path = os.path.relpath('/home/safety', '/home')
print(relative_path)

path = ('/home/safety/Python-Projects/README.md')
print(os.path.dirname(path))
print(os.path.basename(path))

# Print both directory name and basename
calcuFilePath = ('/home/safety/Python-Projects/README.md')
print(os.path.split(calcuFilePath))
print(calcuFilePath.split(os.path.sep))

# Finding files and Folder content
file_size = os.path.getsize('/home/safety/bash/actions.sh')
print(file_size)

list_dir = os.listdir('/home/safety/bash')
print(list_dir)

# Getting the total size of all the files in the specified directory by looping through all the files in the directory
totalSize = 0

for filename in os.listdir('home/safety/bash'):
    totalSize = totalSize + os.path.getsize(os.path.join('/home/safety/bash', filename))
print(totalSize)

