import cmath

def Equation():
    K = input("enter value for a")
    a = int(K)
    N = input("enter value for b")
    b = int(N)
    M = input("enter value for c")
    c = int(M)

    D = (b * b) - (4 * a * c)

    if D > 0:
        print("Real Roots")
        sol_1 = (-b-cmath.sqrt(D))/(2*a)
        sol_2 = (-b+cmath.sqrt(D))/(2*a)
        answer_1 = print(f"The roots of the quadratic equation are {sol_1},{sol_2}")
    
    elif D < 0:
        d = -D
        print("Imaginary Roots")
        if a != 0:
            sol_3 = (-b-cmath.sqrt(d))/(2*a)
            sol_4 = (-b+cmath.sqrt(d))/(2*a)
            answer_2 = print(f"The roots of the quadratic equation are {sol_3},{sol_4}")
        
        else:
            print("Invalid")

    else:
        print("Check the Equation")


Equation()