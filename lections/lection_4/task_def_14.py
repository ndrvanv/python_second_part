def add_two_def(a, b):
    return a + b

add_two_lambda = lambda a, b: a + b

print(add_two_def(23, 23.2))
print(add_two_lambda(2, 44.3))

my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
s_key = sorted(my_dict.items())
s_value = sorted(my_dict.items(), key=lambda x: x[1]) #TODO
print(f'{s_key = } \n {s_value}')