# 使用切片创建副本

my_pizzas = ['durian pizza', 'tomato pizza', 'pineapple pizza']
friend_pizzas = my_pizzas[:]
my_pizzas.append('pepperoni pizza')
friend_pizzas.append('ice cream pizza')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
