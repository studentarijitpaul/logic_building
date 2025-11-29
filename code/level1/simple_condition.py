while True:
    try:

        num = int(input("Enter a number: "))
        if num>0:
            print("The number is positive.")
            break
        if num<0:
            print("The number is negative.")
            break
        if num==0:
            print("The number is zero.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        