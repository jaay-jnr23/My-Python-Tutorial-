#QUESTION ONE -- QUADRATIC EQUATION
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



#QUESTION TWO --- CYLINDER
import math

def Cylinder():
    R = input("Radius of the cylinder in metre\n")
    r = float(R)
    H = input("Height of the cylinder in metre\n")
    h = float(H)
    
    pi = 3.142
    unit = input("In what unit? for both the height and radius M, CM, MM\n")
    if unit == "M":
         Volume = (pi * r * r * h)
         v = str(int(Volume))
         Answer_1 = print(f"The volume of the cylinder is {v} M^3")
        
         CSA = (2 * pi * r * h)
         csa = str(int(CSA))
         Answer_2 = print(f"The curve surface area of the cylinder is {csa} M^2")

         TSA = (2 * pi * r**2) + (2 * pi * r * h)
         tsa = str(int(TSA))        
         Answer_3 = print(f"The total surface area of the cylinder is {tsa} M^2")
    
    elif unit == "CM":
         r_1 = (r * 100)
         h_1 =(h * 100)

         Volume_1 = (pi * r_1 * r_1 * h_1)
         v_1 = str(int(Volume_1))
         Answer_4 = print(f"The volume of the cylinder is {v_1} CM^3")

         CSA_1 = (2 * pi * r_1 * h_1)
         csa_1 = str(int(CSA_1))
         Answer_5 = print(f"The curve surface area of the cylinder is {csa_1} CM^2")

         TSA_1 = (2 * pi * r_1**2) + (2 * pi * r_1 * h_1)
         tsa_1 = str(int(TSA_1))
         Answer_6 = print(f"The total surface area of the cylinder is {tsa_1} CM^2")
    
    elif unit == "MM":
         r_2 = (r * 1000)
         h_2 =(h * 1000)

         Volume_2 = (pi * r_2 * r_2 * h_2)
         v_2 = str(int(Volume_2))
         Answer_7 = print(f"The volume of the cylinder is {v_2} MM^3")

         CSA_2 = (2 * pi * r_2 * h_2)
         csa_2 = str(int(CSA_2))
         Answer_8 = print(f"The curve surface area of the cylinder is {csa_2} MM^2")

         TSA_2 = (2 * pi * r_2**2) + (2 * pi * r_2 * h_2)
         tsa_2 = str(int(TSA_2))
         Answer_9 = print(f"The total surface area of the cylinder is {tsa_2} MM^2")
 
    else:
         print("Invalid Unit")

Cylinder()