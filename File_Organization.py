import os
import shutil

folder = "C:/Users/Downloads"

for file in os.listdir(folder):
    path = os.path.join(folder, file)


    if os.path.isdir(path):
        continue

    ext = file.split('.')[-1]

    ext_folder = os.path.join(folder, ext)
    if not os.path.exists(ext_folder):
        os.mkdir(ext_folder)

    shutil.move(path, os.path.join(ext_folder, file))

print("Files organized by type!")
