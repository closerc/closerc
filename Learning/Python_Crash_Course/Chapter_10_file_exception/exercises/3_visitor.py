# 写入文件

filename = r'Chapter_10_test_file\guest.txt'
name = input("Please enter your name: ")
with open(filename, 'w') as file_object:
    file_object.write(name)
