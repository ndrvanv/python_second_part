def mutable(data: list[int]) -> list[int]:
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'In func {data =}') # Для демонстрации
    return data

my_list = [2, 34, 3, 5]
print(f'In main {my_list =}')
new_list = mutable(my_list)
print(f'{my_list = }\t{new_list = }')