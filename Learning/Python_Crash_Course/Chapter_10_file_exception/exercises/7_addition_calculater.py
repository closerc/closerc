# 处理错误后继续运行

print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst num: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond num: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        msg = "You should enter a number not a char."
        print(msg)
    else:
        print(answer)
