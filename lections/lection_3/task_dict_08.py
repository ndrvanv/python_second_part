my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.items())

for turple_data in my_dict.items(): #bad
    print(turple_data)
    print(f'{turple_data[0] = } value before 100 {100 - turple_data[1]}')

print()

for key, value, in my_dict.items(): # good
    print(f'{key = } value before 100 - {100 - value}')