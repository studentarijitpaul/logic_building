while True :

    try:
        num = int(input('enter a number'))

        if num >= 1 and num < 10 :
        
            print('its a single digit number...')
            break
        elif num >= 10 and num < 100:  
    
            print('its a double digit number...')
            break
        elif num >= 100 :
            print('its a multidigit number.... ')
            break
        
    except ValueError :
        print("invaild input Please check yor input")
