# 使用任意数量的实参

def make_sandwich(*toppings):
    """概述顾客点的三明治
    """
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_sandwich('ham')
make_sandwich('ham', 'egg')
make_sandwich('ham', 'egg', 'tomato')
