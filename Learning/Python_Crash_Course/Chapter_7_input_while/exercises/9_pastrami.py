# while循环删除列表中的特定值

sandwich_orders = ['tuna sandwich', 'pastrami', 'egg sandwich', 'pastrami', 'pork sandwich', 'pastrami']
finished_sandwiches = []

print("The pastrami in the deli is sold out!")
# 删除三明治订单列表中的pastrami
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# 完成每个三明治订单
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + ".")
    finished_sandwiches.append(sandwich)

# 显示所以已完成订单
print("\nThere are the finished sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
