import os


def del_file(path):
    files = os.listdir(path)
    for file in files:
        c_path = os.path.join(path, file)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)


file_path = r"D:\东南亚月数据\shopee月数据"
del_file(file_path)
