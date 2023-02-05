# 写入文件

filename = 'guest.txt'
name = input("Please enter your name: ")
with open(filename, 'w') as file_object:
    file_object.write(name)
