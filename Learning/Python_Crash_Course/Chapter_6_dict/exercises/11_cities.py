# 字典嵌套字典

cities = {
    'wuhan': {
        'country': 'china',
        'population': 'twelve million',
        'fact': 'It is a heroic city',
    },
    'tokyo': {
        'country': 'japan',
        'population': 'thirteen million',
        'fact': 'It have Mount Fuji',
    },
    'paris': {
        'country': 'france',
        'population': 'twelve million',
        'fact': 'It is an art city',
    },
}

for city, city_info in cities.items():
    print("\nCity: " + city.title())
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact']
    print("\tCountry: " + country)
    print("\tPopulation: " + population)
    print("\tFact: " + fact)
