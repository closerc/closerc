# 定义带参数的函数

def favorite_book(book_name):
    """打印一条消息

    Args:
        book_name (str): a book
    """
    print("One of my favorite books is " + book_name.title() + ".")


favorite_book('three body')
