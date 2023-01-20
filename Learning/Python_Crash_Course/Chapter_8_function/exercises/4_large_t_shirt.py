# 默认值

def make_shirt(size='L', word='I love Python'):
    """显示T恤尺码和字样

    Args:
        size (str, optional): 尺码. Defaults to 'L'.
        word (str, optional): 字样. Defaults to 'I love Python'.
    """
    print("The size of T-shirt is " + size + ", and the words are " + word + ".")


make_shirt()
make_shirt('M')
make_shirt(word='I love C')
