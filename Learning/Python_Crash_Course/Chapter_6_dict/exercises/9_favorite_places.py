# 字典嵌套列表

favorite_places = {
    'tan wei': ['wuhan', 'jingmen'],
    'dong yuan': ['dali'],
    'long liping': ['changsha', 'nanjing', 'qingdao'],
}

for friend_name, places in favorite_places.items():
    if len(places) == 1:
        print("\n" + friend_name.title() + "'s favorite place is:")
    else:
        print("\n" + friend_name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())
