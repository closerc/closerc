# 编写函数，传递任意数量的关键字参数

def make_car(manufacturer, model, **car_info):
    """创建一个字典，包含我们知道的有关车的所有信息

    Args:
        manufacturer (str): 制造商
        model (str): 型号
    """
    car_profile = {}
    car_profile['manufacturer'] = manufacturer
    car_profile['model'] = model
    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
