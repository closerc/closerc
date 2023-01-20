# 返回简单值
'''
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名

    Args:
        first_name (str): 名
        last_name (str): 姓
    """
    full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
'''

# 让实参变成可选的


def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名

    Args:
        first_name (str): 名
        last_name (str): 姓
        middle_name (str, optional): 中间名. Defaults to ''.
    """
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musicain = get_formatted_name('jimi', 'hendrix')
print(musicain)
musicain = get_formatted_name('john', 'hooker', 'lee')
print(musicain)
