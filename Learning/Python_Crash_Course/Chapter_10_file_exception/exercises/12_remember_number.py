# 将写入和读取程序合二为一

import json


def get_stored_number():
    """如果存储了数字，就获取它"""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number


def get_new_number():
    """提示用户输入数字"""
    number = input("Enter your favorite number: ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
    return number


def show_number():
    """向用户显示数字"""
    number = get_stored_number()
    if number:
        print("I know your favorite number! It's " + number + ".")
    else:
        number = get_new_number()
        print("I know your favorite number! It's " + number + ".")


show_number()
