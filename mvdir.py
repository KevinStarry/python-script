import os
import shutil

# /num/withdir/files

path = os.getcwd()
print('Current path:', path)
# print(os.path.abspath(os.path.dirname(__file__)))
files = list()
files = os.listdir(path)
for file in files:
    if os.path.isdir(file):
        for _ in os.path.isdir(file):
            shutil.move(_,file)
