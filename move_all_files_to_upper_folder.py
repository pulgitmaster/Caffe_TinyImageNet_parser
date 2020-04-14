from os.path import join, isdir, exists
from os import listdir, rmdir
from shutil import move

root = 'train'

dir_name = []
with open("wnids.txt") as f:
    for line in f:
        dir_name.append(line[:-1])

print(dir_name)
for _dir in dir_name:
    root = 'train/' + _dir
    print('move imgs -> root : ' + root)
    if(isdir(join(root, 'images')) is not True) :  continue
    for fileName in listdir(join(root, 'images')):
        move(join(root, 'images', fileName), join(root, fileName))
    rmdir(join(root, 'images'))