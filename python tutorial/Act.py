import cmath

def Quadratic():
    A = input("enter value for a")
    a = int(A)
    B = input("enter value for b")
    b = int(B)
    C = input("enter value for c")
    c = int(C)

    D = (b * b) - (4 * a * c)

    if D > 0:
        print("Real Roots")
        solve_1 = (-b-cmath.sqrt(D))/(2*a)
        Sol_1 = str(solve_1)
        solve_2 = (-b+cmath.sqrt(D))/(2*a)
        Sol_2 = str(solve_2)
        ans_1 = print("The roots of the equation are" + Sol_1 + "and" + Sol_2)
    
    elif D < 0:
        d = -D
        print("Imaginary Roots")
        if a != 0:
            solve_3 = (-b-cmath.sqrt(d))/(2*a)
            Sol_3 = str(solve_3)
            solve_4 = (-b+cmath.sqrt(d))/(2*a)
            Sol_4 = str(solve_4)
            ans_2 = print("The roots of the equation are" + Sol_3 + "and" + Sol_4)
        
        else:
            print("Invalid Entries")

    else:
        print("Not a quadratic equation")


Quadratic()