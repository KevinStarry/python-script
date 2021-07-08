import os
import shutil

# /num/withdir/files
root_dir = os.getcwd()
print('Current path:', root_dir)
# print(os.path.abspath(os.path.dirname(__file__)))
first_dirs = os.listdir(root_dir)
for _ in first_dirs:
    if os.path.isdir(_):
        second_dirs = os.listdir(_)
        for _ in os.listdir(second_dirs):
            shutil.move(_,root_dir)

