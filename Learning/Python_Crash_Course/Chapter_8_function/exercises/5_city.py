# 默认值

def describe_city(city, country='China'):
    """显示城市所属国家

    Args:
        city (str): 城市
        country (str, optional): 国家. Defaults to 'China'.
    """
    print(city.title() + " is in " + country.title() + ".")


describe_city('wuhan')
describe_city('beijing')
describe_city('tokyo', 'japan')
