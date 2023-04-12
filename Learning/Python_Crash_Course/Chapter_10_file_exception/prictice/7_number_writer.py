# 数据写入json文件

import json
numbers = [2, 3, 5, 7, 11, 13]
filename = r'Chapter_10_test_file\numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
