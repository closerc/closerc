# while 循环    询问年龄输出相应票价

prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("The ticket is free!")
    elif age <= 12:
        print("The ticket price is 10 dollars.")
    elif age > 12:
        print("The ticket price is 15 dollars.")
