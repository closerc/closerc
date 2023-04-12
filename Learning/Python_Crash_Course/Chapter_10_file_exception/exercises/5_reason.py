# 写入文件

filename = r'Chapter_10_test_file\reason.txt'
with open(filename, 'a') as file_object:
    while True:
        reason = input("Why do you like programming? ")
        if reason == 'q':
            break
        file_object.write(reason + '\n')
