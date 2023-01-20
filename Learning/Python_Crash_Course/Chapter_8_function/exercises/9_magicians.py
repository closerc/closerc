# 传递列表

def show_magicians(magicians):
    """打印列表中每个魔术师的名字

    Args:
        magicians (list): 魔术师列表
    """
    for magician in magicians:
        print(magician.title())


magicians = ['john', 'marie', 'carolina']
show_magicians(magicians)
