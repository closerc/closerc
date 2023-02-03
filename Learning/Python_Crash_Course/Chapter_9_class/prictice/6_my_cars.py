# 导入模块中多个类

from car import Car, ElecticCar
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElecticCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
