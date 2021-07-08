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
        second_dirs = os.listdir(second_path)
        for _ in second_dirs:
            if os.path.isdir(_):
                third_path = os.path.abspath(_)
                print(f'third path is:{third_path}\n')
                third_dirs = os.listdir(third_path)
                shutil.move(third_path,first_path)
