# input()  int()

number = input("How many people have dinner? ")
number = int(number)
if number > 8:
    print("\nThere are no empty tables.")
else:
    print("There is a table available.")
