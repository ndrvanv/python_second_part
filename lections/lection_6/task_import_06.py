from super_module import *

SIZE = 49.5

print(f'{SIZE = }\n {result = }')
#print(f'{x = }') #NameError: name 'x' is not defined
#print(f'{_secret = }') #NameError: name '_secret' is not defined
print(f'{func(100, 200) = }\n{randint(10, 20) = }')

def func(a: int, b: int) -> int:
    return a + b

print(f'{func(100, 200) = }')