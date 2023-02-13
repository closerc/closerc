def get_formatted_name(first, last, middle=''):
    """生成格式整齐的全名

    Args:
        first (str): 名
        last (str): 姓
        middle (str, optional): 中间名 Default to ''.
    """
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
