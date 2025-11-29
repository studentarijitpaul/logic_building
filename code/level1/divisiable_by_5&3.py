while True:
    try:
        num = int(input("enter a number:  "))
        if num%5==0 and num %3 == 0:
            print("the number is divisiable by 5 and 3")
            print(num)
            break
        else:
            print("the number is not divisiable by 5 and 3 ")
    except ValueError as e:
        print("invalid input. please enter a valid integer.")
        print(e)