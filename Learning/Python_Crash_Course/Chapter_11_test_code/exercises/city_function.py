def get_city_country(city, country, population=''):
    """生成类似City Country的字符串

    Args:
        city (str): 城市名
        country (str): 国家名
    """
    if population:
        formatted_name = city.title() + ' ' + country.title() + '-population' + ' ' + str(population)
    else:
        formatted_name = city.title() + ' ' + country.title()
    return formatted_name
