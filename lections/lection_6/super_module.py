from random import randint

__all__ = ['func', '_secret'] # Перечисление для импоритированияиииииии

SIZE = 100
_secret = 'qwerty'
__top_secret = 'q1eqwe123234lsdkf'

def func(a: int, b: int) -> str:
    x = f'В диапазоне от х{a} до {b} получили {randint(a, b)}'
    return x

result = func(1, 7)