pwd = 'text'
res = input('Input password: ')
if res == pwd :
    print("Access granted")
    my_math = int(input('2 + 2 = '))
    if 2 + 2 == my_math:
        print('Math is correct!')
    else:
        print('But be careful')
else:
    print('Access denied')
print('Work completed')