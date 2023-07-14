#Локальные переменные
def func (y: int) -> int:
    x = 10 # локальная перменная внутри функции
    x += 10
    print(f'In func {x = }')
    return x + 1

x = 42
print(f'In main { x = }')
y = func(x)
print(f'{x = }\t {y = }')


