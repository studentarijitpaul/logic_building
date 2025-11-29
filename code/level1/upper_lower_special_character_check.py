while True:
    try:
        user_input = input("enter a Character or a number:")

        if user_input.isupper():
            print("the entered character is an uppercase character")
            break
        elif user_input.islower():
            print("the entered character is a lowercase character")
            break
        elif user_input.isdigit():
            print("the entered is a digit")
            break
        else:
            print("the entered character is a special character")
            break
    except ValueError:
        print("invalid input. please try again")