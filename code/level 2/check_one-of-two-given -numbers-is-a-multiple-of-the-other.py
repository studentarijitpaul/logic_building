num1 = int(input("entar your first number:"))
num2 = int(input("enter your second number:"))
if num1 % num2 == 0 or num2 % num1 == 0:
    print("One of the given numbers is a multiple of the other.")
else:
    print("Neither of the given numbers is a multiple of the other.")
