#Словарь
a = {'one': 42, 'two': 3.14, 'ten': 'Hello World!'}
b = dict(one=42, two=3.14, ten = 'Hello World!')
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello World!')])
print(a==b==c)
print()

# Пример добвалния нового в словарь
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
x = 10
my_dict['ten'] = x
print(my_dict)