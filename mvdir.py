import os
import shutil
# /num/withdir/files
first_path = os.getcwd()
print(f'current path:{first_path}\n')
# print(os.path.abspath(os.path.dirname(__file__)))
first_dirs = os.listdir(first_path)
for _ in first_dirs:
    if os.path.isdir(_):
        second_path = os.path.abspath(_)
        print(f'second path is:{second_path}\n')
        shutil.move(second_path,first_path)
