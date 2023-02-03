# 创建 User 类

class User():
    """用户简介"""
    def __init__(self, first_name, last_name, age, location):
        """初始化用户各项属性

        Args:
            first_name (str): 名
            last_name (str): 姓
            age (int): 年龄
            location (str): 所在地
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        """打印用户信息摘要"""
        print("--User Profile--")
        print("first_name: " + self.first_name.title())
        print("last_name: " + self.last_name.title())
        print("age: " + str(self.age))
        print("location: " + self.location.title())

    def greet_user(self):
        """向用户发出个性化问候"""
        full_name = self.first_name + ' ' + self.last_name
        print("Hello, " + full_name.title() + "!")


user_0 = User('liping', 'long', 29, 'xiaogan')
user_1 = User('wei', 'tan', 27, 'wuhan')

user_0.describe_user()
user_0.greet_user()
user_1.describe_user()
user_1.greet_user()
