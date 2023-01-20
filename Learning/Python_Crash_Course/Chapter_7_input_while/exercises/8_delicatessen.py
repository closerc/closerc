# while 遍历列表

# 创建一个三明治订单列表
# 创建一个已完成订单的空列表
sandwich_orders = ['tuna sandwich', 'egg sandwich', 'pork sandwich']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + ".")
    finished_sandwiches.append(sandwich)

print("\nThere are the finished sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
