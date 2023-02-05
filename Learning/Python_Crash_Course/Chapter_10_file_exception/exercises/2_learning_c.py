# 单词替换

with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    new_line = line.replace('Python', 'C')
    print(new_line.rstrip())
