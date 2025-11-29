while True :
    try:
        num = int(input("Enter a number: "))
        if num % 2 ==0:
            print("the number is even")
            break
        else:
            print("the number is odd")
            break
    except ValueError:
        print("invalid input. khanki integer ta de")