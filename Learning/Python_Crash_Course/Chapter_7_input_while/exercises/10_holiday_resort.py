# while循环使用输入填充字典

# 创建存储调查结果的空字典
responses = {}
# 创建调查是否继续标志
polling_active = True
# 获取调查
while polling_active:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    # 结果写入字典
    responses[name] = place
    # 询问是否继续调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# 显示调查结果
print("\n--- Poll Result---")
for name, response in responses.items():
    print(name.title() + " woule like to go to " + response.title() + ".")
