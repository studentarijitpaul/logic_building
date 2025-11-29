while True:
    try:
        num = int(input("enter a number: "))
        length = len(str(num))
        if length !=4 :
            print("please enter a valid 4 digit year")
            continue
        if num % 4 == 0 and length == 4:
            print("the yera is a leap year")
            break
        else:
                print("the year is not a leap year")
    except ValueError:
        print("invalid input. khanki")