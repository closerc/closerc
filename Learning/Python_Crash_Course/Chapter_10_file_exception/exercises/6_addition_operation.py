# 处理数值错误

print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

first_number = input("\nFirst num: ")
second_number = input("\nSecond num: ")

try:
    answer = int(first_number) + int(second_number)
except ValueError:
    msg = "You should enter a number not a char."
    print(msg)
else:
    print(answer)
