# 尝试使用本章所有函数处理列表

# 城市列表
cities = ['wuhan', 'beijing', 'shanghai', 'guangzhou', 'shenzhen']

# 末尾添加 append()
cities.append('chengdu')
print("Here is the new list:")
print(cities)

# 插入元素 insert()
cities.insert(3, 'chongqin')
print("Here is the new list:")
print(cities)

# 删除语句 del
del cities[0]
print("Here is the new list:")
print(cities)

# 删除元素并可以使用值 pop() 可以指定位置
last_city = cities.pop()
print("The last append city is " + last_city + '.')
print("Here is the new list:")
print(cities)

# 根据值删除元素 reverse()
cities.remove('beijing')
print("Here is the new list:")
print(cities)

# 永久性排序 sort() 逆序参数 reverse=True
cities.sort()
print("Here is the new list:")
print(cities)

# 临时性排序 sorted() 逆序参数 reverse=True
print("Here is the new list:")
print(sorted(cities))

# 倒序元素列表 reverse()
cities.reverse()
print("Here is the new list:")
print(cities)

# 获悉列表长度 len()
print("Here is " + str(len(cities)) + " cities")
