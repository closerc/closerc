# 将实例用作属性

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
        self.login_attempts = 0     # 登录尝试次数

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


class Privilege():
    """模拟管理员权限"""
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        """初始化管理员权限的属性"""
        self.privileges = privileges

    def show_privileges(self):
        """显示管理员权限"""
        print("--Administrator Privileges--")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """特殊的用户——管理员"""
    def __init__(self, first_name, last_name, age, location):
        """初始化管理员的属性"""
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privilege()


admin = Admin('liping', 'long', 29, 'xiaogan')
admin.privileges.show_privileges()
