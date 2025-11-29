while True :

    try:
        num = int(input(' enter a 4 digit no : '))
        l_digit = num%10
        num = (num //10 )//10
        f_digit = num // 10

        if l_digit == f_digit :
            print(f" In this 4 digit number last and first one is equal")
            break
        else:
            print(f" In this 4 digit number last and first one is not eaual")
        
    except ValueError :
        print(" invaild number ")

