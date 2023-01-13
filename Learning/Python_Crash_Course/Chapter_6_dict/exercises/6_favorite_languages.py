# 遍历字典

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

inverstigation_list = ['jen', 'edward', 'phil', 'marie', 'carolina']

for name in inverstigation_list:
    if name in favorite_languages.keys():
        print(name.title() + ", thank you for taking the poll.")
    else:
        print(name.title() + ", please take our poll!")
