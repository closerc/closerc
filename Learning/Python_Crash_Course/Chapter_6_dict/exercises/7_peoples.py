# 列表嵌套字典

people_0 = {
    'first_name': 'wei',
    'last_name': 'tan',
    'age': 26,
    'city': 'wuhan',
}

people_1 = {
    'first_name': 'yuan',
    'last_name': 'dong',
    'age': 28,
    'city': 'wuhan',
}

people_2 = {
    'first_name': 'liping',
    'last_name': 'long',
    'age': 28,
    'city': 'xiaogan',
}

peoples = [people_0, people_1, people_2]

for people in peoples:
    print(people)
