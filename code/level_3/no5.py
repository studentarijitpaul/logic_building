while True:
    try:
        num  =int (input("enter a number : "))
        l_digit = num%10
        if num % 7 == 0 or l_digit == 7 :
            print(" This number is a multiple of 7 or ends with 7")
            break
        else :
            print(" This number is not a multiple of 7 or ends with 7")
            break
    
    except ValueError :
        print("invaild input")

        
