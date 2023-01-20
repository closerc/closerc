# while 循环    输入披萨配料

prompt = "\nPlease enter pizza toppings:"
prompt += "\n(Enter 'quit' when you are finished) "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print("We will add " + message + " to the pizza!")
