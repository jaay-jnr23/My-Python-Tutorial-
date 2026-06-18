import math

def Cylinder():
    R = input("Radius of the cylinder in metre\n")
    r = float(R)
    H = input("Height of the cylinder in metre\n")
    h = float(H)
    pi = 3.142

    Volume = (pi * r * r * h)
    v = str(int(Volume))
    Answer_1 = print(f"The volume of the cylinder is {v} metre cube")

    CSA = (2 * pi * r * h)
    csa = str(int(CSA))
    Answer_2 = print(f"The curve surface area of the cylinder is {csa} metre square")

    TSA = (2 * pi * r**2) + (2 * pi * r * h)
    tsa = str(int(TSA))
    Answer_3 = print(f"The total surface area of the cylinder is {tsa} metre square")

Cylinder()
