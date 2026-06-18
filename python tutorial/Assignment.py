import cmath

def Q_Equation():
    A = input("enter value for a\n")
    a = float(A)
    B = input("enter value for b\n")
    b = float(B)
    C = input("enter value for c\n")
    c = float(C)
    D = (b**2) - (4*a*c)
    
    if D < 0:
         d = -D
         print("Imaginary Roots")
         
         if a != 0:
            x3 = (-b +cmath.sqrt(d))/(2*a)
            x4 = (-b -cmath.sqrt(d))/(2*a)
            answer_1 = print(f"The Root of the quadratic equation are {x3},{x4}")
        
         else:
            print("Can not be simplify, not a quadratic equation")
    
    elif D > 0:
        print("Real Roots")
        x1 = (-b-cmath.sqrt(D))/(2*a)
        x2 = (-b+cmath.sqrt(D))/(2*a)
        answer_2 = print(f"The Root of the quadratic equation are {x1},{x2}")
    elif D == 0:
        print("Same Roots")
        print(-b / 2 * a)
    else:
        print("Invalid Input or Not a Quadratic Equation")

Q_Equation()