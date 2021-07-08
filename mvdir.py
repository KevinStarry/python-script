import os

path = os.getcwd()
print('Current path:', path)
# print(os.path.abspath(os.path.dirname(__file__)))
files = list()
files = os.listdir(path)
for file in files:
    if os.path.isdir(file):
        print('it is a dir:',file)
    else:
        print('it is a file:',file)
