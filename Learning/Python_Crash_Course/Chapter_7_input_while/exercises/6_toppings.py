# 以另一种方式编写 while 循环

prompt = "\nPlease enter pizza toppings:"
prompt += "\n(Enter 'quit' when you are finished) "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print("We will add " + message + " to the pizza!")
