# 切片

players = ['charles', 'martina', 'michael', 'florence', 'eli']
# 前三个元素
print("Here are the first players on my team:")
for player in players[:3]:
    print(player.title())

# 第二个到第四个元素
print(players[1:4])

# 没有指定第一个索引，自动从列表开头开始
print(players[:4])

# 没有指定第二个索引，自动到列表末尾
print(players[2:])

# 负数索引，输出最后三名队员
print(players[-3:])
