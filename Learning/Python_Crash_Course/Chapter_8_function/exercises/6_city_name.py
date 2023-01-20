# 返回字符串

def city_country(city, country):
    """返回城市以及所属国家

    Args:
        city (str): 城市
        country (str): 国家
    """
    city_country_name = city + ' ' + country
    return city_country_name.title()


city_country_pair = city_country('wuhan', 'china')
print(city_country_pair)
city_country_pair = city_country('paris', 'france')
print(city_country_pair)
city_country_pair = city_country('tokyo', 'japan')
print(city_country_pair)
