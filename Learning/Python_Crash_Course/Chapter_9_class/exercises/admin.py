"""一组可用于表示管理员的类"""

from user_1 import User


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
