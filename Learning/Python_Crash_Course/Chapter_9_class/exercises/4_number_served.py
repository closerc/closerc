# 修改属性

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
        self.number_served = 0

    def describe_restaurant(self):
        """描述餐馆名字与拥有的菜肴类型"""
        print("Restaurant's name is " + self.restaurant_name.title() + ".")
        print("Restaurant's cuisine is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        """指出餐馆是否营业"""
        print("The restaurant is open.")

    def print_number_served(self):
        """打印就餐人数信息"""
        print("Number of diners is " + str(self.number_served) + ".")

    def set_number_served(self, number):
        """将就餐人数设置指定的值"""
        self.number_served = number

    def increment_number_served(self, num):
        """将就餐人数增加指定的值"""
        self.number_served += num


restaurant = Restaurant('kfc', 'fried chicken')
restaurant.print_number_served()
restaurant.number_served = 10
restaurant.print_number_served()
restaurant.set_number_served(20)
restaurant.print_number_served()
restaurant.increment_number_served(5)
restaurant.print_number_served()
