import os


def del_file(path):
    files = os.listdir(path)
    for file in files:
        c_path = os.path.join(path, file)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)


file_path = r'D:\shopee月数据\2023\shopee月数据_2 - 副本'
del_file(file_path)
