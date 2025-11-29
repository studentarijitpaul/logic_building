while True:    
        try:
            character = str(input("enter a character:"))
            if (character >='a' and character <= 'm' ):
                print("The given character is lies between a-m.")
                break
            elif(character >='n' and character <='z'):
                print('the given character lies between n-z.')
                break
        except ValueError:
            print("invalid input, enter a lowercase alphabetic character.")