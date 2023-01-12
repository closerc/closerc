# 类似对象组成的字典

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

# 遍历字典
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# 遍历字典中的键 keys()
for name in favorite_languages.keys():      # keys() 可省略，默认遍历字典的键
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

# 使用 keys() 检查
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# 按顺序遍历字典中的键
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# 遍历字典中的值 values() 集合 set() 元素独一无二
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
