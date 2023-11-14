import os


def get_filename(path):
    files = os.listdir(path)
    for file in files:
        c_path = os.path.join(path, file)
        if os.path.isdir(c_path):
            get_filename(c_path)
        else:
            filename = os.path.basename(file).split('.')[0]
            print(filename)


file_path = r'D:\lazada'
get_filename(file_path)
