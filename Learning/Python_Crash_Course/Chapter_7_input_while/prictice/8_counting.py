# continue 忽略余下的代码，返回循环开头

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)
