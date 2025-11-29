while True:
    try:
        num = int(input("Enter a number: "))
        x,y,z = 0,0,0
        if 100 <= num <= 999:
            x= num // 100 
            y = (num //10) %10
            z= num % 10
            print(f"Digits: {x}, {y}, {z}")
        if x > y and x > z:
            print(f"Middle number is largest: {x}")
            break
        elif y > x and x < z:
            print(f"middle number is smallest: {x}")
            
        else:   
            print(f"neither largest nor smallest: {x}")
    except ValueError:
        print("Invalid input. Please enter a three-digit number.")
        
        

    