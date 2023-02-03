# 导入模块中的类

from car import ElecticCar
my_tesla = ElecticCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
