# 单词替换

filename = r'Chapter_10_test_file\learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    new_line = line.replace('Python', 'C')
    print(new_line.rstrip())
