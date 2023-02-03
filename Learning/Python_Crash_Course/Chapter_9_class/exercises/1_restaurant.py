# 创建 Restautant 类

class Restaurant():
    """模拟餐馆营业"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restaurant_name和cuisine_type

        Args:
            restaurant_name (str): 餐馆名字
            cuisine_type (str): 菜肴类型
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """描述餐馆名字与拥有的菜肴类型"""
        print("Restaurant's name is " + self.restaurant_name.title() + ".")
        print("Restaurant's cuisine is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        """指出餐馆是否营业"""
        print("The restaurant is open.")


restaurant = Restaurant('KFC', 'fried chicken')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
