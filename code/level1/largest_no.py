while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        num3 = int(input("Enter third number: ")) 
        print("the largest number is " ,max(num1, num2, num3))
        break
    except valueError:
        print("invalid input. please enter a valid integer.")