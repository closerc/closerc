# 写入访客记录

filename = 'guest_book.txt'
with open(filename, 'w') as file_object:
    while True:
        name = input("Please enter your name: ")
        if name == 'q':
            break
        print("Hello " + name + "!")
        file_object.write(name + '\n')
