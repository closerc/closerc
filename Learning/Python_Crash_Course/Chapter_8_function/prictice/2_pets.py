# 位置实参

def describe_pet(animal_type, pet_name):
    """显示宠物的信息

    Args:
        animal_type (str): 宠物类型
        pet_name (str): 宠物名字
    """
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# 关键字实参
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# 默认值


def describe_pets(pet_name, animal_type='dog'):
    """显示宠物的信息

    Args:
        pet_name (str): 宠物名字
        animal_type (str, optional): 宠物类型. Defaults to 'dog'.
    """
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pets('willie')
