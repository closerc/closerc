# 定义函数，使用不同方式调用

def make_shirt(size, word):
    """显示T恤尺码和字样

    Args:
        size (str): 尺码
        word (str): 字样
    """
    print("The size of T-shirt is " + size.title() + ", and the words are " + word + ".")


make_shirt('m', 'hello')
make_shirt(size='m', word='hello')
