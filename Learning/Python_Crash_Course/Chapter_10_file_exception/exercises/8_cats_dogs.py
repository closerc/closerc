# 处理读取文件错误

def read_file(filename):
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        print(contents)


filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    read_file(filename)
