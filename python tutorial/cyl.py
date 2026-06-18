import math

def Cylinder():
    K = input("Radius of the cylinder in metre\t")
    R = int(K)
    J = input("Height of the cylinder in metre\t")
    H = int(J)
    pi = 3.142

    Volume = (pi * R * R * H)
    V = str(int(Volume))
    Sol_1 = print("The volume of the cylinder" + " " + V + " " + "CM*3")

    CSA = (2 * pi * R * H)
    csa = str(int(CSA))
    Sol_2 = print("The curve surface area of the cylinder is" + " " + csa + " " + "metre square")

    TSA = (2 * pi * R * R) + (2 * pi * R * H)
    tsa = str(int(TSA))
    SOl_3 = print(f"The total surface area of the cylinder is" + " " + tsa + " " + "metre square")

Cylinder()