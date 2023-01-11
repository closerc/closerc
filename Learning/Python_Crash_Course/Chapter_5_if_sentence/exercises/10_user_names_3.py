# 检查用户名

current_users = ['eric', 'carolina', 'marie', 'admin', 'andrew']
new_users = ['Daivid', 'Carolina', 'Mary', 'KAISY', 'ANDREW']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + " is used, you need enter a different user name.")
    else:
        print(new_user + " is not used.")
