def quadratic_equations(a: int | float, b: int | float, c: int | float):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return (-b + d ** 0.5) / (2 * a), (-b -d ** 0.5) / (2 * a)
    if d == 0:
        return -b / ( 2 * a)
    return None
    
print(quadratic_equations(2, -3, -9))