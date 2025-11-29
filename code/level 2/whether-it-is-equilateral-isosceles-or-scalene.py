def calculate_triangle_side(a,b,c):
    if (a+b)>c and(a+c)>b and (b+c)>a:
        return( "Valid Triangle")

    else:
        return "Invalid Triangle"
# Example usage:
while True:
    try:
            side1 = float(input("enter side 1:"))
            side2 = float(input("enter side 2:"))
            side3 = float(input("enter side 3:"))
            result = calculate_triangle_side(side1,side2,side3) 
            print(result)
            if result == "Valid Triangle":
                if side1==side2==side3:
                    print("the tringle is equilateral")
                    break
                elif (side1 ==side2 and side1 != side3 ) or (side2==side3 and side2 !=side1) or (side3 ==side1 and side3 !=side2):
                    print("the tringle is isosceles")
                    break
                elif side1 !=side2 and side2 != side3 and side3 != side1:
                    print("the tringle is scalene")
                    break
            
    except ValueError:
            print("invalid input, please enter numeric values only")

