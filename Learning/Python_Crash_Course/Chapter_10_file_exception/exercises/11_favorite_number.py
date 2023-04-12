# 使用json模块存储和读取数据

import json

filename = r'Chapter_10_test_file\favorite_number.json'
number = input("Enter your favorite number: ")
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)

with open(filename) as f_obj:
    number = json.load(f_obj)
    print("I know your favorite number! It's " + number + ".")
