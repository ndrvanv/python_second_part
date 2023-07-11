pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}')

data = [3254, 3453456456, 23453456, 3454, 234234, 345345]
for item in data:
    print(f'{item:>10}')

num = 2 * pi * data[1]
print(f'{num = :_}')