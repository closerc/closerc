# 读取json文件

import json
filename = r'Chapter_10_test_file\numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)
