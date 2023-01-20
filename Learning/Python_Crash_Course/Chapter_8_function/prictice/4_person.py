# 返回字典

def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息

    Args:
        first_name (str): 名
        last_name (str): 姓
        age (str, optional): 年龄. Defaults to ''.

    Returns:
        _type_: dict
    """
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)
