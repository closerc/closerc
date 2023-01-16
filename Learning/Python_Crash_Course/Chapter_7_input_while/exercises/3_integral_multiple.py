# 10的整倍数

number = input("Enter a number, I'll tell you whether this number is an integral multiple of 10. ")
number = int(number)
if number % 10 == 0:
    print("This number " + str(number) + " is an integral multiple of 10.")
else:
    print("This number " + str(number) + " is not an integral multiple of 10.")
