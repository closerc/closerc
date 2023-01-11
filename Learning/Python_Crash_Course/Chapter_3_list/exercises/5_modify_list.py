# 修改嘉宾名单

name_list = ['tan wei', 'du jinbo', 'long liping', 'dong yuan']
print("I would like to invite " + name_list[0].title() + " to dinner.")
print("I would like to invite " + name_list[1].title() + " to dinner.")
print("I would like to invite " + name_list[2].title() + " to dinner.")
print("I would like to invite " + name_list[3].title() + " to dinner.")
print(name_list[3].title() + " can't come!")

name_list[3] = 'dengchao'

print("I would like to invite " + name_list[0].title() + " to dinner.")
print("I would like to invite " + name_list[1].title() + " to dinner.")
print("I would like to invite " + name_list[2].title() + " to dinner.")
print("I would like to invite " + name_list[3].title() + " to dinner.")
