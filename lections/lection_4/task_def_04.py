def no_mutable(a: int) -> int:
    a += 1
    print(f'In func {a = }') #Для демонстрации
    return a

a = 42
print(f'In main {a = }')
x = no_mutable(a)
print(f'{a = }\t{x = }')