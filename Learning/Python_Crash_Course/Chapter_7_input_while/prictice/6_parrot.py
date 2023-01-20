# while 循环    让用户选择何时退出

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
""" message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
 """

# 添加标志 优化 while 循环
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
