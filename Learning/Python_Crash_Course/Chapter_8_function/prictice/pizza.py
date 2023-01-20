# 传递任意数量的实参 * 创建一个元组

def make_pizza(size, *toppings):
    """概述要制作的披萨

    Args:
        size (int): 披萨尺寸
    """
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
