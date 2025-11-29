while True:
    try:    


            num = str(input("Enter three digit number:"))
            if len(num) != 3:
                print("Please enter a three digit number.")
                continue
            if (num[0] != num[1]) and(num[1] != num[2]) and (num[0] != num[2])  :
                print(f"In this number {num} all digits are distinct.")
               
            else:
                print("All digits are not distinct.")
    except ValueError:
            print("Invalid input, please enter numeric values.")
    

  