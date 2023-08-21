import pytest
def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Не допускается деление на ноль")
    return a / b

def test_division():
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(0, 5) == 0
    assert divide_numbers(-10, -2) == 5

def test_division_by_zero():
    with pytest.raises(ValueError):
        divide_numbers(10, 0)

if __name__ == "__main__":
    if __name__ == '__main__':
        pytest.main
