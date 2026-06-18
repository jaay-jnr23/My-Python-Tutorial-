import math

def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    root_1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root_2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root_1, root_2


a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))


roots = solve_quadratic_equation(a, b, c)


print(f'Roots of the quadratic equation: {roots}')



