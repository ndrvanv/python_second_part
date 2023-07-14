#Глобальные переменные
def func(y: int) -> int:
    global x   # объявление глобальной переменной с помощью
    x += 100
    print(f'In func {x = }')
    return y + 1

x = 42
print(f'In main { x = }')
y = func(x)
print(f'{x = }\t {y = }')