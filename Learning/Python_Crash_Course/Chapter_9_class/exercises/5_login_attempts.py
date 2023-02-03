# 修改属性

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
        self.login_attempts = 0     # 用户登录尝试次数

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

    def print_login_attempts(self):
        """打印用户登录尝试次数"""
        print("Number of user login attempts is " + str(self.login_attempts) + ".")

    def increment_login_attempts(self):
        """将登录尝试次数的值加1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将登录尝试次数重置为0"""
        self.login_attempts = 0


user = User('liping', 'long', 29, 'xiaogan')
user.print_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.print_login_attempts()
user.reset_login_attempts()
user.print_login_attempts()
