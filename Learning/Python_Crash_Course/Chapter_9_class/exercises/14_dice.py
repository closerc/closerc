# 创建模拟骰子的类

from random import randint


class Die():
    """模拟骰子"""
    def __init__(self, sides=6):
        """初始化骰子的属性"""
        self.sides = sides

    def roll_die(self):
        """打印位于1和骰子面数之间的随机数"""
        x = randint(1, self.sides)
        print(str(x))


dice_6 = Die()
for i in range(10):
    dice_6.roll_die()

dice_10 = Die(10)
for i in range(10):
    dice_10.roll_die()

dice_20 = Die(20)
for i in range(10):
    dice_20.roll_die()
