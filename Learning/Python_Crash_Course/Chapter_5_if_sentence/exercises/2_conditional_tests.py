# 条件测试

car = 'subaru'
print(car == 'subaru')
print(car != 'subaru')

car = 'Subaru'
print(car.lower() == 'subaru')

num_0 = 21
num_1 = 43
print(num_0 == num_1)
print(num_0 != num_1)
print(num_0 < num_1)
print(num_0 > num_1)
print(num_0 <= num_1)
print(num_0 >= num_1)

print(num_0 > 12 and num_1 > 12)
print(num_0 > 54 or num_1 < 45)

cars = ['subaru', 'audi', 'bmw', 'toyato']
print(car in cars)
print(car not in cars)
