# 处理错误不发出消息

def read_file(filename):
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)


filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    file_path = r'Chapter_10_test_file'
    file_path = file_path + '\\' + filename
    read_file(file_path)
