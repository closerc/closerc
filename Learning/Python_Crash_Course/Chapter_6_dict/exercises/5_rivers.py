# 循环遍历字典的键和值

rivers = {
    'nile': 'egypt',
    'yangtze river': 'china',
    'amazon river': 'brazil',
}

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

print("\nThere are the rivers:")
for river in rivers.keys():
    print(river)

print("\nThere are the countries:")
for country in rivers.values():
    print(country)
