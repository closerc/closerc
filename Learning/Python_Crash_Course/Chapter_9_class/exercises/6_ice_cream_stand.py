# 编写 IceCreamStand 子类

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


class IceCreamStand(Restaurant):
    """独特的冰淇淋小店"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化冰淇淋小店的属性"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'vanilla', 'chocolates', 'durian']

    def show_flavors(self):
        """显示冰淇淋口味"""
        print("--Ice Cream--")
        for flavor in self.flavors:
            print(flavor)


ice_cream_stand = IceCreamStand('turkiye', 'ice cream')
ice_cream_stand.show_flavors()
