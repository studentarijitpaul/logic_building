
while True:
    try:
            month_no = int(input("enter month number between 1-12:"))
            year = int(input("enter year:"))
            check_leap_year = year % 4
            converted_into_string =len(str(year))
            if month_no < 1 or month_no > 12:
                print('please enter a valid month number between 1-12')
                continue
            if converted_into_string !=4:
                print('please enter a valid year')
                
            if check_leap_year == 0:
                print('it is a leap year..... please enter a not leap year')
            else:
                print(calendar.month(year, month_no))
                break
    except ValueError:
            print("invalid input, please enter numeric values for month and year.")