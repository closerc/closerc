import os
import shutil

filelist = []
rootdir = r'D:\shopee月数据\2023\shopee月数据_2 - 副本'
filelist = os.listdir(rootdir)

for file in filelist:
    file_path = os.path.join(rootdir, file)
    if os.path.isfile(file_path):
        os.remove(file_path)
    elif os.path.isdir(file_path):
        shutil.rmtree(file_path, True)
