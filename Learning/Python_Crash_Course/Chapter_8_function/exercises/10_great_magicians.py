# 修改列表

def show_magicians(magicians):
    """打印列表中每个魔术师的名字

    Args:
        magicians (list): 魔术师列表
    """
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    """在每个魔术师名字前加入字样 the Great

    Args:
        magicians (list): 魔术师列表
    """
    great_magicians = []
    # 对每个元素添加字样并存储进 great_magicians
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # 将修改添加字样后的元素放回原列表
    for great_magician in great_magicians:
        magicians.append(great_magician)


magicians = ['john', 'marie', 'carolina']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)
