# 传递列表

def greet_users(names):
    """向列表中的每位用户都发出简单的问候

    Args:
        names (list): 用户列表
    """
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'marot']
greet_users(usernames)
