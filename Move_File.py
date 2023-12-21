import os
import shutil

from_dir = '/Users/dhruvmakhija/Downloads/Project102'
to_dir = '/Users/dhruvmakhija/Desktop/Dhruv_Makhija/Document_Files'

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + 'image_files'
        path3 = to_dir + '/' + 'image_files' + '/' + file_name

        if os.path.exists(path2):
            print('moving...' + file_name)
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print('moving...' + file_name)
            shutil.move(path1, path3)