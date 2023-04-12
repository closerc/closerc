# 读取用户数据

import json

filename = r'Chapter_10_test_file\username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
print("Welcome back, " + username + "!")
