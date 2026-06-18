import math

def equation( a, b, c ):
    d = b**2 - 4 * a * c

    sqrtval = math.sqrt(abs(d))

    if d > 0:
        print("Different Roots")
        print((-b + sqrtval)/(2 * a))
        print((-b - sqrtval)/(2 * a))

    elif d == 0:
        print("Same Root")
        print(-b / (2 * a))

    else:
        print("Complex Roots")
        print(-b / (2 * a), " + i", sqrtval)
        print(-b / (2 * a), " - i", sqrtval)
        
equation()