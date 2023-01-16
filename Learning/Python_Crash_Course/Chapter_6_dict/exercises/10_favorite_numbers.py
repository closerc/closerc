# 字典嵌套列表

favorite_numbers = {
    'tan wei': [1, 2, 4],
    'dong yuan': [4, 5, 7],
    'long liping': [7],
    'du jinbo': [0, 2, 6],
    'deng chao': [5, 6, 1],
}

for friend_name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print("\n" + friend_name.title() + "'s favorite number is:")
    else:
        print("\n" + friend_name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + str(number))
