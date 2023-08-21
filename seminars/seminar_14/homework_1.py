
# Пример использования Docktest на Python
def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

if __name__ == "__main__":
    import doctest
    doctest.testmod()